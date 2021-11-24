import easyocr
import os

get = easyocr.Reader(['en'])

img_pth = [rf"../NIC Images/{img}" for img in os.listdir(r'../NIC Images/')]


for img in img_pth:
    print("_______________________________________________")
    print(f"Image {img}")
    img_file = get.readtext(img)
    for a, b, c in img_file:
        print(b)  
    print("_______________________________________________")

