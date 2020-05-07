from PIL import Image
import os

def image_resizer(img,h,w):
    im = Image.open(img)
    resize = im.resize((h,w),Image.ANTIALIAS)
    resize.save('Resized_'+img)

os.chdir("E:/memory")
image_resizer('/ts.jpg',400,400)