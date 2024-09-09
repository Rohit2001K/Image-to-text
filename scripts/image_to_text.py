import pytesseract
import numpy as np
import cv2
from PIL import Image
from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = (r'C:\Users\XIOXIO\AppData\Local\Programs\Tesseract-OCR\tesseract.exe') 


def process_image(image):
    pic= Image.open(image)
    a='THIS IS WORKED'
    result=pytesseract.image_to_string(pic)
    if result=='':
        result='Image is not supported'
        return result,a
    return result,a

  
        

        

