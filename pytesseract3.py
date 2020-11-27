from PIL import Image
import pytesseract
import re
import os

# 테서랙트 옵션 조정
# custom_oem_psm_config1 = r'--oem 0 --psm 6'
custom_oem_psm_config2 = r'--oem 1 --psm 6'
custom_oem_psm_config3 = r'--oem 2 --psm 6'

# 테서랙트로 이미지에서 텍스트 추출
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

### psm 바꾸기
# 0    Orientation and script detection (OSD) only.
# 1    Automatic page segmentation with OSD.
# 2    Automatic page segmentation, but no OSD, or OCR.
# 3    Fully automatic page segmentation, but no OSD. (Default)
# 4    Assume a single column of text of variable sizes.
# 5    Assume a single uniform block of vertically aligned text.
# 6    Assume a single uniform block of text.
# 7    Treat the image as a single text line.
# 8    Treat the image as a single word.
# 9    Treat the image as a single word in a circle.
# 10    Treat the image as a single character.
# 11    Sparse text. Find as much text as possible in no particular order.
# 12    Sparse text with OSD.
# 13    Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract-specific.

text1 = pytesseract.image_to_string(Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\imageotsu.jpg"), lang="kor")
print(" psm 차이 알아보기 ")
print("--기본 옵션 oem 3 --psm 3-----------")
print(text1)

text2 = pytesseract.image_to_string(Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\imageotsu.jpg"), lang="kor",config=custom_oem_psm_config1)
print("--oem 3 --psm 6--------------------")
print(text2)

text3 = pytesseract.image_to_string(Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\imageotsu.jpg"), lang="kor",config=custom_oem_psm_config2)
print("--oem 3 --psm 7--------------------")
print(text2)

### oem 바꾸기 (결과 ; 1번 LSTM만 가능)

# 0    Legacy engine only.
# 1    Neural nets LSTM engine only.
# 2    Legacy + LSTM engines.
# 3    Default, based on what is available

# text1 = pytesseract.image_to_string(Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\imageotsu.jpg"), lang="kor",config=custom_oem_psm_config1)
# print(" oem 차이 알아보기(psm은 6으로 설정) ")
# print("--oem 0 --psm 6-----------")
# print(text1)

text2 = pytesseract.image_to_string(Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\imageotsu.jpg"), lang="kor",config=custom_oem_psm_config2)
print("--oem 1 --psm 6--------------------")
print(text2)

# text3 = pytesseract.image_to_string(Image.open(r"C:\Users\alfot\Desktop\ocr_pytesseract\img\imageotsu.jpg"), lang="kor",config=custom_oem_psm_config3)
# print("--oem 2 --psm 6--------------------")
# print(text2)
