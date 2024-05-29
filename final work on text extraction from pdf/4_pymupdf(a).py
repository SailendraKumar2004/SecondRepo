import fitz  # PyMuPDF
from langdetect import detect, LangDetectException
import re

# Define a function to clean the extracted text
def clean_text(text):
    # Remove control characters and ensure the text is XML compatible
    clean_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    return clean_text

# Define the path to the PDF file
pdf_path = r"D:\all files\Academics And Skills\B.TECH\2ND Year\internship at IIIT H\text extraction form pdf\Re_ Selenium Resources and Site Links\Deposition Tiruvarur TNTV040000392022_5_2024-04-16.pdf"
pdf = fitz.open(pdf_path)

# Open a text file for writing
with open('4_pymupdf(a).txt', 'w', encoding='utf-8') as txt_file:
    # Iterate over the PDF pages
    for page in pdf:
        text = page.get_text()
        print(text)
        cleaned_text = clean_text(text)

        # Print the extracted and cleaned text
        print("Extracted Text:")
        print(cleaned_text)
        
        # Write the cleaned text to the text file
        txt_file.write(cleaned_text + "\n\n")  # Separate sections by new lines

        # Detect the language of the text if it is not empty
        if cleaned_text.strip():
            try:
                detected_language = detect(cleaned_text)
                print(f"Detected Language: {detected_language}")
                # Write the detected language at the end of the text file
                txt_file.write(f"Detected Language: {detected_language}\n\n")
            except LangDetectException as e:
                print(f"Language detection failed: {e}")
                txt_file.write("Language detection failed.\n\n")
        else:
            print("No text extracted from this page.")
            txt_file.write("No text extracted from this page.\n\n")

print("End of processing with PyMuPDF library")






# import fitz  # PyMuPDF
# from docx import Document
# from langdetect import detect, LangDetectException
# import re

# # Define a function to clean the extracted text
# def clean_text(text):
#     # Remove control characters and ensure the text is XML compatible
#     clean_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
#     return clean_text

# # Create a new Document
# doc = Document()

# # Define the path to the PDF file
# pdf_path = r"D:\all files\Academics And Skills\B.TECH\2ND Year\internship at IIIT H\text extraction form pdf\Re_ Selenium Resources and Site Links\Deposition Tiruvarur TNTV040000392022_5_2024-04-16.pdf"
# pdf = fitz.open(pdf_path)

# # Iterate over the PDF pages
# for page in pdf:
#     text = page.get_text()
#     print(text)
#     cleaned_text = clean_text(text)

#     # Print the extracted and cleaned text
#     print("Extracted Text:")
#     print(cleaned_text)
#     if text.strip():
#         try:
#             detected_language = detect(text)
#             print(f"Detected Language: {detected_language}")
#         except LangDetectException as e:
#             print(f"Language detection failed: {e}")
#     else:
#         print("No text extracted from the PDF.")
#     # Detect the language of the cleaned text if it is not empty
#     if cleaned_text.strip():
#         try:
#             detected_language = detect(cleaned_text)
#             print(f"Detected Language: {detected_language}")
#         except LangDetectException as e:
#             print(f"Language detection failed: {e}")
#     else:
#         print("No text extracted from the PDF.")

#     # Add the cleaned text to the Word document
#     doc.add_paragraph(cleaned_text)

# # Save the document
# doc.save('4_pymupdf(a).docx')

# print("End of processing with PyMuPDF library")
