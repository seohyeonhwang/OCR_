import os
import cv2
import numpy as np

_MAX_HISTO_ = 256

# 오버플로우 방지를 위한 함수
def cut_range(img_src, min_val=0, max_val=255):
    img_cut = np.zeros(img_src.shape)
    for h in range(img_src.shape[0]):
        for w in range(img_src.shape[1]):
            if img_src[h,w] < min_val:
                img_cut[h,w] = min_val
            elif img_src[h,w] > max_val:
                img_cut[h,w] = max_val
            else:
                img_cut[h,w] = img_src[h,w]
    return img_cut

#원본 영상에 가우시안 노이즈를 추가한 결과를 반환하는 함수(float64 타입을 반환)
#원본 영상과 정규분포의 표준편차 값을 인자로 받음

def add_gaussian_noise(img_src, std):

    src_height = img_src.shape[0]
    src_width = img_src.shape[1]
    #노이즈가 발생한 이미지를 저장할 변수 생성(오버플로우를 방지하기 위해 float64형 사용)
    img_noisy = np.zeros(img_src.shape, dtype=np.float64)
    for h in range(src_height):
        for w in range(src_width):
            #평균0 표준편차가 1인 정규분포를 가지는 난수 발생
            std_norm = np.random.normal()
            #인자로 받은 표준편차와 곱
            random_noise = std*std_norm
            #원본 값에 발생한 난수에 따른 노이즈를 합
            img_noisy[h,w] = img_src[h,w] +random_noise
    #노이즈가 발생한 이미지를 반환
    return img_noisy

def img_aver(img1, img2):
    src_height = img1.shape[0]
    src_width = img1.shape[1]
    img = np.zeros(img1.shape, dtype=np.float64)
    for h in range(src_height):
        for w in range(src_width):
            img[h,w] = (img1[h,w] + img2[h,w])/2

    return img

def img_aver2(img1, img2, img3, img4):
    src_height = img1.shape[0]
    src_width = img1.shape[1]
    img = np.zeros(img1.shape, dtype=np.float64)
    for h in range(src_height):
        for w in range(src_width):
            img[h,w] = (img1[h,w] + img2[h,w] + img3[h,w] + img4[h,w])/4

    return img

#현재 실행되고 있는 경로 값을 얻어서 이미지 경로를 조합
#cur_path = os.getcwd()
#img_src = "moon.jpg"
#img_src_path = os.path.join(cur_path, img_src)
img_src_path = r"C:\Users\adrie\Desktop\imageotsu.jpg"

#원본 상태로 이미지 읽기
img_src = cv2.imread(img_src_path, cv2.IMREAD_GRAYSCALE)

#가우시안 노이즈를 생성
img_gn = add_gaussian_noise(img_src, 64)
img_gn2 = add_gaussian_noise(img_src, 64)
img_gn3 = add_gaussian_noise(img_src, 64)
img_gn4 = add_gaussian_noise(img_src, 64)
img_N2 = img_aver(img_gn, img_gn2)
img_N4 = img_aver2(img_gn, img_gn2, img_gn3, img_gn4)

#값의 범위를 unit8형에 맞게 자르고 형변환
img_gn = np.uint8(cut_range(img_gn))
img_gn2 = np.uint8(cut_range(img_gn2))
img_N2 = np.uint8(cut_range(img_N2))
img_N4 = np.uint8(cut_range(img_N4))

cv2.imshow("N=1", img_gn) #N=1일 떄
cv2.imshow("N=2", img_N2) #N=2일 떄
cv2.imshow("N=4", img_N4) #N=4일 떄
cv2.waitKey()
cv2.destroyAllWindows()

from PIL import Image
import pytesseract
import re
cv2.imwrite(r"C:\Users\adrie\Desktop\imagegaussian.jpg",img_N4)

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open(r"C:\Users\adrie\Desktop\imagegaussian.jpg"), lang="kor")
# print(text)
text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>\{\}`\'…》]', '', text)
print(text.replace(" ", ""))