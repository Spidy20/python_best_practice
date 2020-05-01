#1st method
from PIL import Image

path = 'E:/memory/spidy.jpg'
pdf = Image.open(path)
pdf.save('E:memory/spidy.pdf')

#2nd method

import img2pdf

with open("E:/memory/spidy.pdf",'wb') as f:
    f.write(img2pdf.convert('E:/memory/spidy.jpg'))