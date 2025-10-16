# Deployment Guide for Streamlit Cloud

## Prerequisites

1. **GitHub Account**: You need a GitHub account to host your code
2. **Streamlit Cloud Account**: Sign up at [share.streamlit.io](https://share.streamlit.io)
3. **OpenAI API Key**: Get your API key from [OpenAI Platform](https://platform.openai.com)

## Step-by-Step Deployment

### 1. Prepare Your Repository

1. Create a new repository on GitHub
2. Upload all the project files to your repository
3. Make sure your repository structure looks like this:
   ```
   your-repo/
   ├── app.py
   ├── streamlit_app.py
   ├── requirements.txt
   ├── packages.txt
   ├── config.toml
   ├── .gitignore
   ├── README.md
   └── secrets.toml.example
   ```

### 2. Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click "New app"
3. Connect your GitHub account
4. Select your repository
5. Choose the main file:
   - **Main file path**: `streamlit_app.py` (for Streamlit Cloud)
   - **App URL**: Choose a custom URL or use the default
6. Click "Deploy!"

### 3. Configure Secrets

1. In your Streamlit Cloud dashboard, go to your app
2. Click "Settings" (gear icon)
3. Go to "Secrets" tab
4. Add your OpenAI API key:
   ```toml
   OPENAI_API_KEY = "your_actual_openai_api_key_here"
   ```
5. Click "Save"

### 4. Verify Deployment

1. Your app should be available at `https://your-app-name.streamlit.app`
2. Test the app by uploading a sample PDF
3. Check that data extraction works correctly

## Important Notes

### For Streamlit Cloud:
- Use `streamlit_app.py` as your main file
- The app will automatically install dependencies from `requirements.txt`
- Tesseract OCR will be installed via `packages.txt`
- Environment variables are managed through the Streamlit Cloud secrets

### For Local Development:
- Use `app.py` as your main file
- Create a `.env` file with your OpenAI API key
- Install dependencies: `pip install -r requirements.txt`

## Troubleshooting

### Common Issues:

1. **"Please set your OPENAI_API_KEY" error**:
   - Make sure you've added the API key in Streamlit Cloud secrets
   - Check that the key name is exactly `OPENAI_API_KEY`

2. **OCR not working**:
   - Tesseract is installed via `packages.txt`
   - If issues persist, check the logs in Streamlit Cloud

3. **PDF processing errors**:
   - The app handles both searchable and scanned PDFs
   - Check the console for specific error messages

4. **Memory issues**:
   - Large PDFs might cause memory issues
   - Consider processing files one at a time for very large documents

## Security Notes

- Never commit your `.env` file or `secrets.toml` to version control
- Use Streamlit Cloud secrets for production deployment
- Keep your OpenAI API key secure and don't share it publicly

## Performance Optimization

- The app processes files sequentially to avoid memory issues
- Large PDFs are processed page by page
- Consider upgrading to GPT-4 for better accuracy if needed
