import pymupdf  # Import PyMuPDF
from langdetect import detect

# Open the PDF document
pdf = pymupdf.open("D:\\all files\\Academics And Skills\\B.TECH\\2ND Year\\internship at IIIT H\\text extraction form pdf\\Re_ Selenium Resources and Site Links\\21916_2012_36_1501_23210_Judgement_29-Jul-2020_HIN.pdf")

# Open a text file for writing
with open('1_pymupdf.txt', 'w', encoding='utf-8') as txt_file:
    for page in pdf:  # iterate the document pages
        text = page.get_text()  # get plain text encoded as UTF-8
        print(text)
        detected_language = detect(text)
        print(f"Detected Language: {detected_language}")
        txt_file.write(text + "\n\n")  # Write the text to the file with a newline for separation

print("End of processing with PyMuPDF library")




'''import pymupdf
from docx import Document
from langdetect import detect
pdf=pymupdf.open("D:\\all files\\Academics And Skills\\B.TECH\\2ND Year\\internship at IIIT H\\text extraction form pdf\\Re_ Selenium Resources and Site Links\\21916_2012_36_1501_23210_Judgement_29-Jul-2020_HIN.pdf")
# Create a new Document
doc = Document()

for page in pdf: # iterate the document pages
  text = page.get_text() # get plain text encoded as UTF-8
  print(text)
  detected_language = detect(text)
  print(f"Detected Language: {detected_language}")
  doc.add_paragraph(text)

doc.save('1_pymupdf.docx')

print("end of proceesing with pymupdf library")'''
# input("press enter to continue to another library")

# import fitz  # PyMuPDF
# from langdetect import detect



# # Using a raw string
# doc = fitz.open(r"C:\Users\ganes\Downloads\Re_ Selenium Resources and Site Links\21916_2012_36_1501_23210_Judgement_29-Jul-2020_HIN.pdf")

# for page in doc:  # iterate the document pages
#     text = page.get_text()  # get plain text encoded as UTF-8
#     print(text)  # printing the text to check the output
#     x=detect(text)
#     print(x)

# print("end of fitz library")

