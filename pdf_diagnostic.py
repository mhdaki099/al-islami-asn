#!/usr/bin/env python3
"""
PDF Diagnostic Script - Helps debug PDF processing issues
"""

import streamlit as st
import PyPDF2
import pdfplumber
import fitz  # PyMuPDF
import io
from PIL import Image

def diagnose_pdf(pdf_file):
    """Diagnose PDF file and show detailed information"""
    st.subheader("🔍 PDF Diagnostic Report")
    
    try:
        # Get file info
        pdf_file.seek(0)
        file_size = len(pdf_file.read())
        pdf_file.seek(0)
        
        st.info(f"📁 File: {pdf_file.name}")
        st.info(f"📏 Size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
        
        # Test PyPDF2
        st.markdown("### PyPDF2 Analysis")
        try:
            pdf_file.seek(0)
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            st.success(f"✅ PyPDF2: {len(pdf_reader.pages)} pages")
            
            # Try to extract text from first page
            if len(pdf_reader.pages) > 0:
                first_page_text = pdf_reader.pages[0].extract_text()
                if first_page_text.strip():
                    st.success(f"✅ Text found: {len(first_page_text)} characters")
                    with st.expander("First page text preview"):
                        st.text(first_page_text[:500] + "..." if len(first_page_text) > 500 else first_page_text)
                else:
                    st.warning("⚠️ No text found in first page")
        except Exception as e:
            st.error(f"❌ PyPDF2 failed: {str(e)}")
        
        # Test pdfplumber
        st.markdown("### pdfplumber Analysis")
        try:
            pdf_file.seek(0)
            with pdfplumber.open(pdf_file) as pdf:
                st.success(f"✅ pdfplumber: {len(pdf.pages)} pages")
                
                # Try to extract text from first page
                if len(pdf.pages) > 0:
                    first_page_text = pdf.pages[0].extract_text()
                    if first_page_text and first_page_text.strip():
                        st.success(f"✅ Text found: {len(first_page_text)} characters")
                        with st.expander("First page text preview (pdfplumber)"):
                            st.text(first_page_text[:500] + "..." if len(first_page_text) > 500 else first_page_text)
                    else:
                        st.warning("⚠️ No text found in first page")
        except Exception as e:
            st.error(f"❌ pdfplumber failed: {str(e)}")
        
        # Test PyMuPDF
        st.markdown("### PyMuPDF Analysis")
        try:
            pdf_file.seek(0)
            pdf_bytes = pdf_file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            st.success(f"✅ PyMuPDF: {pdf_document.page_count} pages")
            
            # Try to extract text from first page
            if pdf_document.page_count > 0:
                first_page_text = pdf_document[0].get_text()
                if first_page_text.strip():
                    st.success(f"✅ Text found: {len(first_page_text)} characters")
                    with st.expander("First page text preview (PyMuPDF)"):
                        st.text(first_page_text[:500] + "..." if len(first_page_text) > 500 else first_page_text)
                else:
                    st.warning("⚠️ No text found in first page")
                    
                    # Try to get page as image
                    page = pdf_document[0]
                    pix = page.get_pixmap()
                    img_data = pix.tobytes("png")
                    image = Image.open(io.BytesIO(img_data))
                    st.info(f"🖼️ Page as image: {image.size[0]}x{image.size[1]} pixels")
                    
                    # Show the image
                    st.image(image, caption="First page as image", use_column_width=True)
            
            pdf_document.close()
        except Exception as e:
            st.error(f"❌ PyMuPDF failed: {str(e)}")
        
        # OCR Test (if available)
        st.markdown("### OCR Analysis")
        try:
            import pytesseract
            pdf_file.seek(0)
            pdf_bytes = pdf_file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            
            if pdf_document.page_count > 0:
                page = pdf_document[0]
                pix = page.get_pixmap()
                img_data = pix.tobytes("png")
                image = Image.open(io.BytesIO(img_data))
                
                # Try OCR
                ocr_text = pytesseract.image_to_string(image)
                if ocr_text.strip():
                    st.success(f"✅ OCR text found: {len(ocr_text)} characters")
                    with st.expander("OCR text preview"):
                        st.text(ocr_text[:500] + "..." if len(ocr_text) > 500 else ocr_text)
                else:
                    st.warning("⚠️ No text found via OCR")
            
            pdf_document.close()
        except ImportError:
            st.info("ℹ️ OCR not available locally")
        except Exception as e:
            st.error(f"❌ OCR failed: {str(e)}")
        
        # Summary
        st.markdown("### 📋 Summary")
        st.info("""
        **PDF Types:**
        - **Searchable PDF**: Contains selectable text
        - **Scanned PDF**: Image-based, needs OCR
        - **Mixed PDF**: Contains both text and images
        
        **Recommendations:**
        - If text is found: Use searchable PDF methods
        - If no text but image is clear: Use OCR
        - If image is unclear: Try different OCR settings
        """)
        
    except Exception as e:
        st.error(f"❌ Diagnostic failed: {str(e)}")

def main():
    st.title("🔍 PDF Diagnostic Tool")
    st.markdown("Upload a PDF file to diagnose processing issues")
    
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        help="Upload a PDF file to analyze"
    )
    
    if uploaded_file:
        diagnose_pdf(uploaded_file)

if __name__ == "__main__":
    main()
