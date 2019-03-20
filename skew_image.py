'''
Created on 2019. 3. 20.

@author: Won Jong Hyun
'''

import sys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image as im
from PIL import ImageOps
from scipy.ndimage import interpolation as inter

# 스크립트 실행시 인자를 받는다
# sys.argv[0]는 모듈의 파일명이 넘어온다
# 커맨드 창에서 ~~~.py 인자1 인자2 ... 이런식으로 입력
input_file = sys.argv[1]

img = im.open(input_file)

# binary로 변환한다
wd, ht = img.size
pix = np.array(img.convert('1').getdata(), np.uint8)
bin_img = 1 - (pix.reshape(ht, wd) / 255.0)
# plt.imshow(bin_img, cmap='gray')
# plt.savefig('binary.png')

def find_score(arr, angle):
    data = inter.rotate(arr, angle, reshape=False, order=0)
    hist = np.sum(data, axis=1)
    score = np.sum((hist[1:] - hist[:-1]) ** 2)
    return hist, score

# 최대 +-30도 정도 기울어진 문서에 대해 적정 각도를 찾는 것
delta = 1
limit = 30
angles = np.arange(-limit, limit+delta, delta)
scores = []
for angle in angles:
    hist, score = find_score(bin_img, angle)
    scores.append(score)

best_score = max(scores)
# 가장 적정 회전 각도 출력
best_angle = angles[scores.index(best_score)]
print('Best angle: {}'.format(best_angle))

# 기울어진 이미지를 회전시킨다
data = inter.rotate(bin_img, best_angle, reshape=False, order=0)
# 까만 배경에 흰 글씨 이미지로 출력됨
img = im.fromarray((255 * data).astype("uint8")).convert("RGB")
# 흰 배경에 검은 글씨를 만들기 위해 흑백 반전
img_inv = ImageOps.invert(img)
img_inv.save('data/skew_correct/skew_corrected06.png')
'''
실제 노트에다 손으로 쓴 글씨의 경우 배경까지 색상 처리되어 글자 인식이 잘 안되는 경우가 많다.
바이너리화 하기 전에 최대한 글자 부분만 검은색에 배경의 흰 색으로 처리하는 것이 관건
'''