import pdfplumber
from pdf2image import convert_from_path
from PIL import Image
import pytesseract
from bs4 import BeautifulSoup

def pdf_to_html(pdf_path, html_path):
    # Convert each page of the PDF to an image
    images = convert_from_path(pdf_path)

    # Extract text and styling information using OCR
    full_text = ""
    for image in images:
        text = pytesseract.image_to_string(image)
        full_text += text + "\n"

    # Create BeautifulSoup object to generate HTML
    soup = BeautifulSoup(full_text, 'html.parser')
    
    # Write HTML content to file
    with open(html_path, 'w', encoding='utf-8') as html_file:
        html_file.write(soup.prettify())

# Example usage:
pdf_path = 'example.pdf'  # Replace with the path to your PDF file
html_path = 'output.html' # Replace with the desired output HTML file path
pdf_to_html(pdf_path, html_path)
