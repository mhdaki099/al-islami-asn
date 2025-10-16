# 📄 Invoice Data Extractor

A powerful Streamlit application that extracts structured data from invoice PDFs using OpenAI's GPT API. The application handles both searchable PDFs and scanned PDFs (using OCR) and exports the data to formatted Excel files.

## ✨ Features

- **Multi-file upload**: Process multiple PDF files at once
- **Dual PDF processing**: Handles both searchable and scanned PDFs
- **AI-powered extraction**: Uses OpenAI GPT to extract structured data
- **Smart field recognition**: Recognizes various field names and abbreviations
- **Excel export**: Exports extracted data to a professionally formatted Excel file
- **Cloud-ready**: Designed for deployment on Streamlit Cloud
- **Error handling**: Comprehensive error handling and processing logs
- **Progress tracking**: Real-time progress updates during processing

## 📋 Required Fields

The application extracts the following information from invoices:

| Field | Alternative Names |
|-------|------------------|
| PO Number | PO No, Purchase Order, P.O. Number, Order No |
| Item Code | Item No, Product Code, SKU, Part Number, Product ID |
| Description | Product Description, Item Description, Product Name |
| UOM | Unit of Measure, Unit, U/M, Unit Type |
| Quantity | Qty, Amount, Qty Ordered |
| Lot Number | Lot No, Batch Number, Batch No, Lot ID |
| Expiry Date | Exp Date, Expiration Date, Use By Date |
| Mfg Date | Manufacturing Date, Mfg Date, Production Date, Made Date |
| Invoice No | Invoice Number, Inv No, Invoice ID |
| Unit Price | Price per Unit, Unit Cost, Price, Rate |
| Total Price | Line Total, Item Total, Amount |
| Country | Origin Country, Country of Origin, Made In |
| HS Code | HSN Code, Tariff Code, Customs Code |
| Date of Invoice | Invoice Date, Date, Issue Date |
| Customer No | Customer Number, Customer ID, Client No, Account No |
| Payer Name | Payer, Bill To, Billing Name |
| Currency | Curr, Currency Code |
| Supplier Name | Vendor Name, Supplier, Company Name, Seller |
| Total Amount of the Invoice | Grand Total, Total Amount, Invoice Total, Net Total |
| Total VAT or Tax | VAT, Tax, Tax Amount, VAT Amount, Tax Total |

## 🚀 Quick Start

### Local Development

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd al-islami-asn
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   - Copy `env_example.txt` to `.env`
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_openai_api_key_here
     ```

4. **Test the setup**:
   ```bash
   python test_setup.py
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

### Streamlit Cloud Deployment

1. **Push to GitHub**: Push your code to a GitHub repository
2. **Deploy on Streamlit Cloud**:
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Connect your GitHub repository
   - Set the main file to `streamlit_app.py`
   - Add your OpenAI API key in the secrets section
3. **Access your app**: Your app will be available at `https://your-app-name.streamlit.app`

## 📁 Project Structure

```
al-islami-asn/
├── app.py                 # Main application (local development)
├── streamlit_app.py       # Streamlit Cloud version
├── app_enhanced.py        # Enhanced version with better UI
├── requirements.txt       # Python dependencies
├── packages.txt          # System packages for Streamlit Cloud
├── config.toml           # Streamlit configuration
├── secrets.toml.example  # Example secrets file
├── env_example.txt       # Example environment file
├── test_setup.py         # Setup testing script
├── demo.py              # Demo and testing script
├── README.md            # This file
├── DEPLOYMENT.md        # Detailed deployment guide
└── .gitignore          # Git ignore file
```

## 🛠️ Usage

1. **Upload PDFs**: Upload one or multiple PDF files using the file uploader
2. **Configure settings**: Use the sidebar to configure processing options
3. **Extract data**: Click "Extract Data" to process the files
4. **Review results**: Check the extracted data in the table
5. **Download Excel**: Download the formatted Excel file with all data

## 🔧 Technical Details

### PDF Processing
- **Searchable PDFs**: Uses `pdfplumber` for optimal text extraction
- **Scanned PDFs**: Uses `PyMuPDF` + `Tesseract OCR` for image-based text extraction
- **Fallback methods**: Multiple extraction methods ensure maximum compatibility

### AI Integration
- **Model**: OpenAI GPT-3.5-turbo
- **Prompt engineering**: Optimized prompts for accurate data extraction
- **Error handling**: Robust error handling for API failures

### Excel Export
- **Professional formatting**: Headers with colors and borders
- **Auto-sizing**: Automatic column width adjustment
- **Data validation**: Proper data type handling

## 🧪 Testing

Run the test suite to verify your setup:

```bash
# Test all components
python test_setup.py

# Test with demo data
python demo.py
```

## 📊 Performance

- **File size limit**: Configurable (default 10MB)
- **Processing speed**: ~2-5 seconds per PDF depending on complexity
- **Memory usage**: Optimized for cloud deployment
- **Concurrent processing**: Sequential processing to avoid memory issues

## 🚨 Troubleshooting

### Common Issues

1. **"Please set your OPENAI_API_KEY" error**:
   - Ensure your API key is set in `.env` file (local) or Streamlit Cloud secrets
   - Check that the key name is exactly `OPENAI_API_KEY`

2. **OCR not working**:
   - Tesseract is automatically installed on Streamlit Cloud
   - For local development, install Tesseract OCR on your system

3. **PDF processing errors**:
   - Check that the PDF is not password-protected
   - Ensure the PDF contains readable text or clear images

4. **Memory issues**:
   - Reduce the maximum file size limit
   - Process files one at a time for very large documents

## 🔒 Security

- Never commit your `.env` file or `secrets.toml` to version control
- Use Streamlit Cloud secrets for production deployment
- Keep your OpenAI API key secure and don't share it publicly

## 📈 Performance Optimization

- The app processes files sequentially to avoid memory issues
- Large PDFs are processed page by page
- Consider upgrading to GPT-4 for better accuracy if needed
- Use the enhanced version (`app_enhanced.py`) for better UI and error handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter any issues:
1. Check the troubleshooting section above
2. Run the test scripts to identify problems
3. Check the Streamlit Cloud logs for deployment issues
4. Create an issue in the GitHub repository
