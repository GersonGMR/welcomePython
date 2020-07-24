import pytesseract
import cv2

imagen_original = cv2.imread("C:\\Users\\GersonGM\\Documents\\programacion\\images\\testimg.png")
cv2.waitKey(0)

text = pytesseract.image_to_string(imagen_original)
print(text)
