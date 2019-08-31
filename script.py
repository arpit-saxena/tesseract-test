#!/usr/bin/env python3

from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
import os 
from nltk.corpus import stopwords 
import system

def process_PDF_file (pdf_file):
    if os.path.getsize(pdf_file) / 1024 > 1024:
        return -1

    os.system("./do", pdf_file)
    
    initial_ocr = ""
    pages = convert_from_path(pdf_file, 400)
    for page in pages:
        initial_ocr += pytesseract.image_to_string(page)

    stop_words = set(stopwords.words('english'))

    pattern = re.compile('[\W_]+')
    pattern.sub('', string.printable)

    initial_ocr_tokens = 
    filtered_ocr = [w for w in word_tokens if not w in stop_words] 
