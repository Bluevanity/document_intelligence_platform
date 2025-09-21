import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Users\hp\OneDrive\Documents\Management_api\.env\Lib\site-packages\tesseract"
text = pytesseract.image_to_string(Image.open('Screenshot (226).png'))
print(text)