#!/usr/bin/env python3
"""
PDF Type Detection Script - Determines if PDF is searchable or scanned
"""

import streamlit as st
import PyPDF2
import pdfplumber
import fitz  # PyMuPDF
from PIL import Image
import io

def detect_pdf_type(pdf_file):
    """Detect if PDF is searchable or scanned"""
    st.subheader("🔍 PDF Type Detection")
    
    try:
        # Get file info
        pdf_file.seek(0)
        file_size = len(pdf_file.read())
        pdf_file.seek(0)
        
        st.info(f"📁 File: {pdf_file.name}")
        st.info(f"📏 Size: {file_size:,} bytes ({file_size/1024/1024:.2f} MB)")
        
        # Test 1: PyPDF2 text extraction
        st.markdown("### Test 1: PyPDF2 Text Extraction")
        try:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            total_text = ""
            for page_num, page in enumerate(pdf_reader.pages):
                page_text = page.extract_text()
                if page_text:
                    total_text += page_text
            
            if total_text.strip():
                st.success(f"✅ PyPDF2 found text: {len(total_text)} characters")
                with st.expander("PyPDF2 text preview"):
                    st.text(total_text[:500] + "..." if len(total_text) > 500 else total_text)
            else:
                st.warning("⚠️ PyPDF2 found no text")
        except Exception as e:
            st.error(f"❌ PyPDF2 failed: {str(e)}")
        
        # Test 2: pdfplumber text extraction
        st.markdown("### Test 2: pdfplumber Text Extraction")
        try:
            pdf_file.seek(0)
            with pdfplumber.open(pdf_file) as pdf:
                total_text = ""
                for page_num, page in enumerate(pdf.pages):
                    page_text = page.extract_text()
                    if page_text:
                        total_text += page_text
                
                if total_text.strip():
                    st.success(f"✅ pdfplumber found text: {len(total_text)} characters")
                    with st.expander("pdfplumber text preview"):
                        st.text(total_text[:500] + "..." if len(total_text) > 500 else total_text)
                else:
                    st.warning("⚠️ pdfplumber found no text")
        except Exception as e:
            st.error(f"❌ pdfplumber failed: {str(e)}")
        
        # Test 3: PyMuPDF text extraction
        st.markdown("### Test 3: PyMuPDF Text Extraction")
        try:
            pdf_file.seek(0)
            pdf_bytes = pdf_file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            
            total_text = ""
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                page_text = page.get_text()
                if page_text:
                    total_text += page_text
            
            pdf_document.close()
            
            if total_text.strip():
                st.success(f"✅ PyMuPDF found text: {len(total_text)} characters")
                with st.expander("PyMuPDF text preview"):
                    st.text(total_text[:500] + "..." if len(total_text) > 500 else total_text)
            else:
                st.warning("⚠️ PyMuPDF found no text")
        except Exception as e:
            st.error(f"❌ PyMuPDF failed: {str(e)}")
        
        # Test 4: Check if PDF contains images
        st.markdown("### Test 4: Image Analysis")
        try:
            pdf_file.seek(0)
            pdf_bytes = pdf_file.read()
            pdf_document = fitz.open(stream=pdf_bytes, filetype="pdf")
            
            total_images = 0
            for page_num in range(pdf_document.page_count):
                page = pdf_document[page_num]
                image_list = page.get_images()
                total_images += len(image_list)
            
            pdf_document.close()
            
            if total_images > 0:
                st.info(f"🖼️ Found {total_images} images in PDF")
            else:
                st.info("🖼️ No images found in PDF")
        except Exception as e:
            st.error(f"❌ Image analysis failed: {str(e)}")
        
        # Test 5: OCR Test (if available)
        st.markdown("### Test 5: OCR Test")
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
                
                # Try OCR on first page
                ocr_text = pytesseract.image_to_string(image)
                if ocr_text.strip():
                    st.success(f"✅ OCR found text: {len(ocr_text)} characters")
                    with st.expander("OCR text preview"):
                        st.text(ocr_text[:500] + "..." if len(ocr_text) > 500 else ocr_text)
                else:
                    st.warning("⚠️ OCR found no text")
            
            pdf_document.close()
        except ImportError:
            st.info("ℹ️ OCR not available locally")
        except Exception as e:
            st.error(f"❌ OCR failed: {str(e)}")
        
        # Summary
        st.markdown("### 📋 Summary")
        st.info("""
        **PDF Types:**
        - **Searchable PDF**: Contains selectable text (works locally)
        - **Scanned PDF**: Image-based, needs OCR (works on Streamlit Cloud)
        - **Mixed PDF**: Contains both text and images
        
        **Recommendations:**
        - If text is found: Use searchable PDF methods
        - If no text but OCR works: Use OCR methods
        - If neither works: PDF might be corrupted or password-protected
        """)
        
    except Exception as e:
        st.error(f"❌ Detection failed: {str(e)}")

def main():
    st.title("🔍 PDF Type Detection Tool")
    st.markdown("Upload a PDF file to determine if it's searchable or scanned")
    
    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=['pdf'],
        help="Upload a PDF file to analyze"
    )
    
    if uploaded_file:
        detect_pdf_type(uploaded_file)

if __name__ == "__main__":
    main()
