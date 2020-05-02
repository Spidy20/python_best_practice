import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'

def img_to_text(img):
    read = pytesseract.image_to_string(img)
    with open("text.txt",'w') as f:
        f.write(read)
img_to_text("E:/memory/bsort.jpg")
