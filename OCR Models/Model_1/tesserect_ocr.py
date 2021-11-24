import cv2, os
import pytesseract


def ocr_core(img):
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    text = pytesseract.image_to_string(img)
    return text
img_pth = [rf"ocr_project\NIC Images/{img}" for img in os.listdir(r'ocr_project\NIC Images/')]



def get_greyscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def remove_noice(img):
    return cv2.medianBlur(img, 5)

def thresholing(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


for idx,img in enumerate(img_pth):
    img = cv2.imread(img)
    img = get_greyscale(img)
    img = remove_noice(img)
    img = thresholing(img)
    print("-"*20)
    print(f"Image {idx}")
    with open('results.txt', 'a') as f:
        f.write(ocr_core(img))
    print(ocr_core(img))
    print("-"*20)
