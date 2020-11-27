
from PIL import Image
import pytesseract
import re
import cv2
import os
import numpy as np

img = Image.open(r"C:\Users\adrie\Desktop\snackgray.jpg")
img_numpy = np.array(img, 'uint8')
gray = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"C:\Users\adrie\Desktop\nadalgray.png",gray)
#print("All Done")

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open(r"C:\Users\adrie\Desktop\nadalgray.png"), lang="kor")
# print(text)
text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>\{\}`\'…》]', '', text)
print(text.replace(" ", ""))


