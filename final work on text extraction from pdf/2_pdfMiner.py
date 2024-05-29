
from pdfminer.high_level import extract_text
from langdetect import detect
import re

# Define a function to clean the extracted text
def clean_text(text):
    # Remove control characters and ensure the text is XML compatible
    clean_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    return clean_text

# Define the path to the PDF file
pdf_path = "D:\\all files\\Academics And Skills\\B.TECH\\2ND Year\\internship at IIIT H\\text extraction form pdf\\Re_ Selenium Resources and Site Links\\26750_2019_3_1501_20710_Judgement_19-Feb-2020_TEL.pdf"

# Extract text from the PDF
text = extract_text(pdf_path)
print(text)
# Clean the extracted text
cleaned_text = clean_text(text)

# Print the extracted text
print("Extracted Text:")
print(cleaned_text)

# Open a text file for writing
with open('2_pdfMinerText.txt', 'w', encoding='utf-8') as txt_file:
    # Write the cleaned text to the text file
    txt_file.write(cleaned_text)
    
    # Detect the language of the extracted text
    if cleaned_text.strip():  # Check if the cleaned text is not empty
        detected_language = detect(cleaned_text)
        print(f"Detected Language: {detected_language}")
        # Write the detected language at the end of the text file
        txt_file.write(f"\n\nDetected Language: {detected_language}")
    else:
        print("No text extracted from the PDF.")

print("End of processing with pdfminer library")




'''from pdfminer.high_level import extract_text
from langdetect import detect
import re

# Define a function to clean the extracted text
def clean_text(text):
    # Remove control characters and ensure the text is XML compatible
    clean_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    return clean_text

# Define the path to the PDF file
pdf_path = "D:\\all files\\Academics And Skills\\B.TECH\\2ND Year\\internship at IIIT H\\text extraction form pdf\\Re_ Selenium Resources and Site Links\\26750_2019_3_1501_20710_Judgement_19-Feb-2020_TEL.pdf"

# Extract text from the PDF
text = extract_text(pdf_path)

# Clean the extracted text
cleaned_text = clean_text(text)

# Print the extracted text
print("Extracted Text:")
print(cleaned_text)

# Open a text file for writing
with open('2_pdfMinerText.txt', 'w', encoding='utf-8') as txt_file:
    # Write the cleaned text to the text file
    txt_file.write(cleaned_text)
    
    # Detect the language of the extracted text
    if cleaned_text.strip():  # Check if the cleaned text is not empty
        detected_language = detect(cleaned_text)
        print(f"Detected Language: {detected_language}")
        # Write the detected language at the end of the text file
        txt_file.write(f"\n\nDetected Language: {detected_language}")
    else:
        print("No text extracted from the PDF.")

print("End of processing with pdfminer library")'''




'''from pdfminer.high_level import extract_text
from docx import Document
from langdetect import detect
import re

# Define a function to clean the extracted text
def clean_text(text):
    # Remove control characters and ensure the text is XML compatible
    clean_text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)
    return clean_text

# Create a new Document
doc = Document()

# Define the path to the PDF file
pdf_path = "D:\\all files\\Academics And Skills\\B.TECH\\2ND Year\\internship at IIIT H\\text extraction form pdf\\Re_ Selenium Resources and Site Links\\26750_2019_3_1501_20710_Judgement_19-Feb-2020_TEL.pdf"

# Extract text from the PDF
text = extract_text(pdf_path)

# Clean the extracted text
cleaned_text = clean_text(text)

# Print the extracted text
print("Extracted Text:")
print(cleaned_text)

# Add the cleaned text to the Word document
doc.add_paragraph(cleaned_text)

# Detect the language of the extracted text
if cleaned_text.strip():  # Check if the cleaned text is not empty
    detected_language = detect(cleaned_text)
    print(f"Detected Language: {detected_language}")
else:
    print("No text extracted from the PDF.")

# Save the document
doc.save('2_pdfMinerText.docx')
'''