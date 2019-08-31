#!/bin/bash

FINAL_FILENAME="$1.ocr"
TEMP_IMAGE_BASE="$1.temp" #Images with name $1.temp-1.png, etc. are formed

rm $FINAL_FILENAME
pdftoppm $1 $TEMP_IMAGE_BASE -png
for file in ${TEMP_IMAGE_BASE}-*.png
do
	tesseract $file - | tr -d '[:punct:]' | tr -d '[:digit:]' >> $FINAL_FILENAME
done;

# Cleaning temp images
rm ${1}.temp*