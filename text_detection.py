# Text Detection

import cv2
import numpy as np
import pytesseract
import re
from pytesseract import Output
from matplotlib import pyplot as plt

img = cv2.imread(r'C:\Users\adrie\Desktop\medicine.jpg')
d = pytesseract.image_to_data(img, output_type=Output.DICT)
n_boxes = len(d['level'])
for i in range(n_boxes):
    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Text Recognition
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(img, lang = 'kor')
text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>\{\}`\'…》]', '', text)
print(text.replace(" ", ""))