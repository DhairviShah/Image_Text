import pytesseract

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract'
result = pytesseract.image_to_string("trial4.jpg")
print(result)