# Mistral OCR App

The **Mistral OCR App** is a Streamlit-based web application that leverages the [Mistral OCR API](https://docs.mistralai.com/) to extract text from both PDF documents and images. Users can either provide a URL or upload a local file. The app displays the original document (or image) in a preview alongside the extracted OCR results and offers a seamless download option—all without refreshing the page.

### 🚀 Try the Mistral OCR App Live!  

🔗 **Live Demo:** [Mistral OCR App](https://mistralocrai.streamlit.app/)  

Experience the power of **Mistral OCR** in action! Upload PDFs or images and extract text seamlessly with this interactive **Streamlit-based OCR app**.  

## Features

- **Dual File Support:** Process both PDFs and images.
- **Multiple Input Methods:** Choose between URL input or local file uploads.
- **Real-Time Preview:** Display the original file (via an iframe for PDFs or using `st.image` for images).
- **OCR Extraction:** Get OCR results presented in a clean, two-column layout.
- **Downloadable Results:** Download the OCR output with a custom HTML link that avoids a full page refresh.
- **Interactive Interface:** Built with Streamlit for a smooth and interactive user experience.

## Installation

### Prerequisites

- Python 3.7 or later
- [Streamlit](https://streamlit.io/)
- [Mistralai Python Client](https://pypi.org/project/mistralai/)

### Steps

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/AIAnytime/Mistral-OCR-App.git
   cd Mistral-OCR-App
   ```

2. **Create and Activate a Virtual Environment (Optional but Recommended):**

   On macOS/Linux:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Required Dependencies:**

   Create a `requirements.txt` file (if not already present) with:
   ```plaintext
   streamlit
   mistralai
   ```

   Then install them:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your Mistral API Key:**

   The app requires a Mistral API key. Export your API key as an environment variable:

   - On macOS/Linux:
     ```bash
     export MISTRAL_API_KEY=your_api_key_here
     ```

   - On Windows (Command Prompt):
     ```bash
     set MISTRAL_API_KEY=your_api_key_here
     ```

## Usage

To run the app, use the following command:

```bash
streamlit run app.py
```

### How It Works

1. **API Key Entry:**  
   When you launch the app, you'll be prompted to enter your Mistral API key.

2. **File Type & Source Selection:**  
   Choose whether you want to process a **PDF** or an **Image** and select the source type—either via a URL or by uploading a file.

3. **Processing:**  
   Click the **Process** button to send the document to the Mistral OCR API. The app then:
   - Displays a preview of the document in the left column.
   - Shows the extracted OCR results in the right column.
   - Provides a download link for the OCR output.

4. **Download:**  
   Click the download link to save the OCR result as a text file without refreshing the page.

## Code Overview

- **app.py:**  
  The main Streamlit application file that contains the logic for:
  - User input handling (API key, file type, source type)
  - Document preparation (base64 encoding for local uploads)
  - Calling the Mistral OCR API
  - Displaying the preview and OCR results
  - Providing a custom download link

- **README.md:**  
  This file, which provides detailed instructions and documentation for the project.

- **requirements.txt:**  
  A list of the required Python packages.

## Contributing

Contributions are welcome! If you have suggestions or find issues, please feel free to:
- Open an issue in the repository.
- Submit a pull request with improvements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements

- [Streamlit](https://streamlit.io/) for making interactive web app development easy.
- [Mistralai](https://github.com/mistralai) for their powerful OCR API and Python client.

## Contact

For any questions or support, please open an issue in this repository or contact [sonu@aianytime.net].
