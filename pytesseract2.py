from PIL import Image
import pytesseract
import os
import re
import cv2
import numpy as np

## morph와 adaptiveThreshold 이용

# def selectWords(img):
img = Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\propolis1.jpg")
org = np.array(img, 'uint8')

# org = cv2.imread('C:\Users\alfot\Desktop\ocr_pytesseract\img\propolis.jpg', cv2.IMREAD_COLOR)
# org = img
# org = cv2.resize(org, dsize=(0,0), fx=0.5, fy=0.5)
gray = cv2.cvtColor(org, cv2.COLOR_BGR2GRAY)  # ================  1 gray scale로 변환

kernel = np.ones((2, 2), np.uint8)
# kernel2 = np.ones((6, 15), np.uint8)
roi_list = []

morph = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)  # 2 ================ 경계선 찾기
#cv2.imwrite(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\morph_propolis_morGra.jpg",morph)

thr = cv2.adaptiveThreshold(morph, 255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY_INV, 3, 30)  # 3 ================ 임계처리
#cv2.imwrite(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\morph_propolis_thr.jpg",thr)

# morph2 = cv2.morphologyEx(thr, cv2.MORPH_CLOSE, kernel2)  # 4 ================ 뭉게기

# contours, _ = cv2.findContours(morph2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # 5 ================ 특징점 찾기

# org2 = cv2.copyMakeBorder(org, 0, 0, 0, 0, cv2.BORDER_REPLICATE)
# for cnt in contours:
#     try:
#         x, y, w, h = cv2.boundingRect(cnt)
#         if w > 5 and 30 < h < 100:
#             # print(w, h)
#             roi = org2[y:y + h, x:x + w]
#             # cv2.imshow('roi', roi)
#             roi_list.append(roi)
#             cv2.rectangle(org, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#     except Exception as e:
#        pass

# cnt = 0              # print all pieces
'''for r in roi_list:
    cnt += 1
    cv2.imshow(str(cnt), r)'''

cv2.imshow('org', org)
#cv2.imshow('roi_list', roi_list)
cv2.imshow('gray', gray)
cv2.imshow('morph', morph)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 테서랙트로 이미지에서 텍스트 추출
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\morph_propolis_morGra.jpg"), lang="kor")
print(text)
# cv2.imshow('morph2', morph2)
# cv2.imshow('thr', thr)

#    return org, roi_list, gray, morph
