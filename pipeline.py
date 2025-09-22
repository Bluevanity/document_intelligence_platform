import pytesseract
from PIL import Image
import cv2


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

def preprocess_image(path):
    img = cv2.imread(path, 0) #greyscale
    img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC) #upscale
    img = cv2.GaussianBlur(img, (5,5), 0) #noise reduction
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #binarization
    return img 




custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.:/-'

text = pytesseract.image_to_string(preprocess_image('invoice.jpg'), config=custom_config)
print(text)


# Everything seems to work pretty much the same even with image pre-processing.
# Perhaps this will make a difference with more data or images with more text. 

#normal_img = pytesseract.image_to_string(Image.open('invoice.jpg'))
#print("This is wothout opencv: " + normal_img )

#image pre-processing is low and so is accuracy with just normal processes

