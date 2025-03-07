import streamlit as st
import os
import base64
from mistralai import Mistral

st.set_page_config(layout="wide", page_title="Mistral OCR App", page_icon="🖥️")
st.title("Mistral OCR App")
st.markdown("<h3 style color: white;'>Built by <a href='https://github.com/AIAnytime'>AI Anytime with ❤️ </a></h3>", unsafe_allow_html=True)
with st.expander("Expand Me"):
    st.markdown("""
    This application allows you to extract information from pdf/image based on Mistral OCR. Built by AI Anytime.
    """)

# 1. API Key Input
api_key = st.text_input("Enter your Mistral API Key", type="password")
if not api_key:
    st.info("Please enter your API key to continue.")
    st.stop()

# Initialize session state variables for persistence
if "ocr_result" not in st.session_state:
    st.session_state["ocr_result"] = None
if "preview_src" not in st.session_state:
    st.session_state["preview_src"] = None
if "image_bytes" not in st.session_state:
    st.session_state["image_bytes"] = None

# 2. Choose file type: PDF or Image
file_type = st.radio("Select file type", ("PDF", "Image"))

# 3. Select source type: URL or Local Upload
source_type = st.radio("Select source type", ("URL", "Local Upload"))

input_url = ""
uploaded_file = None

if source_type == "URL":
    if file_type == "PDF":
        input_url = st.text_input("Enter PDF URL")
    else:
        input_url = st.text_input("Enter Image URL")
else:
    if file_type == "PDF":
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
    else:
        uploaded_file = st.file_uploader("Upload an Image file", type=["jpg", "jpeg", "png"])

# 4. Process Button & OCR Handling
if st.button("Process"):
    if source_type == "URL" and not input_url:
        st.error("Please enter a valid URL.")
    elif source_type == "Local Upload" and not uploaded_file:
        st.error("Please upload a file.")
    else:
        client = Mistral(api_key=api_key)
        # Prepare the document payload and preview source based on type & source.
        if file_type == "PDF":
            if source_type == "URL":
                document = {
                    "type": "document_url",
                    "document_url": input_url
                }
                preview_src = input_url
            else:
                file_bytes = uploaded_file.read()
                encoded_pdf = base64.b64encode(file_bytes).decode("utf-8")
                document = {
                    "type": "document_base64",
                    "document_base64": encoded_pdf
                }
                preview_src = f"data:application/pdf;base64,{encoded_pdf}"
        else:  # file_type == "Image"
            if source_type == "URL":
                document = {
                    "type": "image_url",
                    "image_url": input_url
                }
                preview_src = input_url
            else:
                file_bytes = uploaded_file.read()
                mime_type = uploaded_file.type
                encoded_image = base64.b64encode(file_bytes).decode("utf-8")
                document = {
                    "type": "image_url",
                    "image_url": f"data:{mime_type};base64,{encoded_image}"
                }
                preview_src = f"data:{mime_type};base64,{encoded_image}"
                st.session_state["image_bytes"] = file_bytes 

        with st.spinner("Processing the document..."):
            ocr_response = client.ocr.process(
                model="mistral-ocr-latest",
                document=document,
                include_image_base64=True
            )
            # Extract OCR results by joining markdown from each OCRPageObject
            try:
                if hasattr(ocr_response, "pages"):
                    pages = ocr_response.pages
                elif isinstance(ocr_response, list):
                    pages = ocr_response
                else:
                    pages = []
                result_text = "\n\n".join(page.markdown for page in pages)
                if not result_text:
                    result_text = "No result found."
            except Exception as e:
                result_text = f"Error extracting result: {e}"
            st.session_state["ocr_result"] = result_text
            st.session_state["preview_src"] = preview_src

# 5. Display Preview and OCR Result if available
if st.session_state["ocr_result"]:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Preview")
        if file_type == "PDF":
            # Embed PDF via iframe
            pdf_embed_html = (
                f'<iframe src="{st.session_state["preview_src"]}" width="100%" '
                f'height="800" frameborder="0"></iframe>'
            )
            st.markdown(pdf_embed_html, unsafe_allow_html=True)
        else:
            # For images, display using st.image
            if source_type == "Local Upload" and st.session_state["image_bytes"]:
                st.image(st.session_state["image_bytes"])
            else:
                st.image(st.session_state["preview_src"])
    
    with col2:
        st.subheader("OCR Result")
        st.write(st.session_state["ocr_result"])
        # Create a custom download link for OCR result
        b64 = base64.b64encode(st.session_state["ocr_result"].encode()).decode()
        href = f'<a href="data:file/txt;base64,{b64}" download="ocr_result.txt">Download OCR Result</a>'
        st.markdown(href, unsafe_allow_html=True)
