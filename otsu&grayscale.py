from PIL import Image
import pytesseract
import re
import cv2
import os
import numpy as np

#그레이 스케일
img = Image.open(r"C:\Users\adrie\Desktop\image.jpg")
img_numpy = np.array(img, 'uint8')
gray = cv2.cvtColor(img_numpy, cv2.COLOR_BGR2GRAY)
cv2.imwrite(r"C:\Users\adrie\Desktop\imagegray.jpg",gray)
#print("All Done")

#오츠 이진화
_MAX_HISTO_ = 256


def calc_histo(img_src):
    histo_info = np.zeros(_MAX_HISTO_)

    src_height = img_src.shape[0]
    src_width = img_src.shape[1]

    for h in range(src_height):
        for w in range(src_width):
            histo_info[img_src[h, w]] += 1
    return histo_info


def draw_histo(histo_info):
    img_histo = np.zeros([256, _MAX_HISTO_], dtype=np.uint8)

    histo_height = img_histo.shape[0]

    max_histo = max(histo_info)

    for i in range(_MAX_HISTO_):
        cv2.line(img_histo, (i, histo_height), (i, int(histo_height - histo_info[i] / max_histo * histo_height)), 255,
                 1)

    return img_histo


# 이진화를 수행하는 함수
def my_thresh(src, thresh_val):
    src_height = np.shape(src)[0]
    src_width = np.shape(src)[1]

    dst = np.zeros(np.shape(src), dtype=np.uint8)
    for h in range(src_height):
        for w in range(src_width):
            dst[h, w] = 0 if src[h, w] <= thresh_val else 255

    return dst


# 오츠 이진화 함수
def otsu_thresh(src):
    src_height = np.shape(src)[0]
    src_width = np.shape(src)[1]

    # 히스토그램 계산
    hist = calc_histo(src)
    # 히스토그램을 정규화 하여 픽셀 값에 대한 등장 확률 계싼
    hist_prob = hist / (src_height * src_width)

    # 픽셀 값 등장 확률을 누적하여 히스토그램 범위에 해당하는 등장확률 chist와
    # 0~255까지 히스토그램에 대해 누적된 픽셀의 평균 픽셀 값 cxhist를 계산
    chist = np.zeros(_MAX_HISTO_)
    cxhist = np.zeros(_MAX_HISTO_)

    chist[0] = hist_prob[0]
    cxhist[0] = 0
    for i in range(1, _MAX_HISTO_):
        chist[i] = chist[i - 1] + hist_prob[i]
        cxhist[i] = cxhist[i - 1] + hist_prob[i] * i

    thresh_val = 0
    max_profit = 0
    # 전체 영상에 대한 평균픽셀값은 cxhist의 256번째 값에 해당
    global_mean = cxhist[_MAX_HISTO_ - 1]

    for i in range(_MAX_HISTO_):
        # 클래스 1에 해당하는 픽셀이 등장할 때까지 continue수행(divide by zero 방지)
        if chist[i] == 0: continue;
        # 각 클래스에 해당하는 픽셀이 등장할 확률 계산
        cls1_prob = chist[i]
        cls2_prob = 1 - chist[i]
        # 더이상 클래스 2로 들어갈 픽셀이 존재하지 않을 경우 종료(divide by zero 방지)
        if cls2_prob == 0: break
        cls1_mean = cxhist[i] / cls1_prob
        cls2_mean = (global_mean - cxhist[i]) / cls2_prob

        # 위에서 말했던 이득함수 구현
        profit = cls1_prob * cls2_prob * (cls1_mean - cls2_mean) ** 2

        # 얻어지는 이득값이 이전의 최대이득값보다 큰 경우 임계깞과 최대이득값을 갱신
        if profit > max_profit:
            max_profit = profit
            thresh_val = i

            # 계산된 값을 사용하여 이진화를 수행한 결과 이미지 반환
    print('thresh_val :', thresh_val)
    return my_thresh(src, thresh_val)


# 현재 실행되고 있는 경로 값을 얻어서 이미지 경로를 조합
cur_path = os.getcwd()
#img_name = 'imagegray.jpg'
#image_path = os.path.join(cur_path, img_name)
image_path = r"C:\Users\adrie\Desktop\imagegray.jpg"

# 그레이스케일로 이미지 읽고 히스토그램 이미지 생성
img_src = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
img_histo_src = draw_histo(calc_histo(img_src))
# 오츠 이진화 수행
img_otsu = otsu_thresh(img_src)

# 이미지 보여주기
cv2.imshow('src', img_src)
cv2.imshow('src_histo', img_histo_src)
cv2.imshow('otsu', img_otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite(r"C:\Users\adrie\Desktop\imageotsu.jpg",img_otsu)


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
text = pytesseract.image_to_string(Image.open(r"C:\Users\adrie\Desktop\imageotsu.jpg"), lang="kor")
# print(text)
text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>\{\}`\'…》]', '', text)
print(text.replace(" ", ""))