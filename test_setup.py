#!/usr/bin/env python3
"""
Test script to verify the setup and dependencies
"""

import sys
import importlib

def test_imports():
    """Test if all required packages can be imported"""
    required_packages = [
        'streamlit',
        'pandas',
        'openai',
        'PyPDF2',
        'pdfplumber',
        'pytesseract',
        'PIL',
        'fitz',
        'openpyxl',
        'dotenv'
    ]
    
    print("Testing package imports...")
    failed_imports = []
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"✅ {package}")
        except ImportError as e:
            print(f"❌ {package}: {e}")
            failed_imports.append(package)
    
    if failed_imports:
        print(f"\n❌ Failed to import: {', '.join(failed_imports)}")
        print("Please install missing packages with: pip install -r requirements.txt")
        return False
    else:
        print("\n✅ All packages imported successfully!")
        return True

def test_openai_key():
    """Test if OpenAI API key is configured"""
    try:
        from dotenv import load_dotenv
        import os
        
        load_dotenv()
        api_key = os.getenv("OPENAI_API_KEY")
        
        if api_key and api_key != "your_openai_api_key_here":
            print("✅ OpenAI API key is configured")
            return True
        else:
            print("❌ OpenAI API key not found or not configured")
            print("Please set your OPENAI_API_KEY in the .env file")
            return False
    except Exception as e:
        print(f"❌ Error checking OpenAI key: {e}")
        return False

def test_tesseract():
    """Test if Tesseract OCR is available"""
    try:
        import pytesseract
        from PIL import Image
        import io
        
        # Create a simple test image
        img = Image.new('RGB', (100, 30), color='white')
        
        # Try to run OCR on the test image
        text = pytesseract.image_to_string(img)
        print("✅ Tesseract OCR is working")
        return True
    except Exception as e:
        print(f"❌ Tesseract OCR error: {e}")
        print("Please install Tesseract OCR on your system")
        return False

def main():
    """Run all tests"""
    print("🔍 Testing Invoice Data Extractor Setup\n")
    
    tests = [
        ("Package Imports", test_imports),
        ("OpenAI API Key", test_openai_key),
        ("Tesseract OCR", test_tesseract)
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n--- {test_name} ---")
        results.append(test_func())
    
    print(f"\n{'='*50}")
    if all(results):
        print("🎉 All tests passed! Your setup is ready.")
        print("\nTo run the app locally:")
        print("  streamlit run app.py")
        print("\nTo run the app for Streamlit Cloud:")
        print("  streamlit run streamlit_app.py")
    else:
        print("❌ Some tests failed. Please fix the issues above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
