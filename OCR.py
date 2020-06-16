# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:36:02 2020

@author: H356727
"""
#https://towardsdatascience.com/optical-character-recognition-ocr-with-less-than-12-lines-of-code-using-python-48404218cccb
#https://github.com/UB-Mannheim/tesseract/wiki

#Importing liabraries/test_branch
import numpy as np
import cv2
import pytesseract


img = cv2.imread(r'C:\Working_Honeywell\New Project\OCR\TEST2.png')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.bitwise_not(gray)


kernel = np.ones((2, 1), np.uint8)
img = cv2.erode(img, kernel, iterations=1)
img = cv2.dilate(img, kernel, iterations=1)
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\H356727\AppData\Local\Tesseract-OCR\tesseract.exe'
out_below = pytesseract.image_to_string(img)
print("OUTPUT:", out_below)

#C:\Users\H356727\AppData\Local\Tesseract-OCR