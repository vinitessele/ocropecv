import cv2
import pytesseract

img = cv2.imread("2.png")

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"

resultado = pytesseract.image_to_string(img)
print(resultado)