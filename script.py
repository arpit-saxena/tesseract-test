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
    
    ocr_text = open(pdf_file + ".ocr", "r")

import glob
def process_subdirectories():
    for filename in glob.iglob('./**/*.pdf', recursive=True):
        process_PDF_file(filename)
