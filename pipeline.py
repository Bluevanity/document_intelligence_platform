import pytesseract
from PIL import Image
import cv2


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

img_cv = cv2.imread('Screenshot (226).png')
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(img_rgb)
print(text)

# Everything seems to work pretty much the same even with image pre-processing.
# Perhaps this will make a difference with more data or images with more text. 