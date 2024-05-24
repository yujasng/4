import time
import numpy as np
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
# TODO 1: Import pyplot & image from matplotlib


def findblack(rgba):
    if (max(rgba)+min(rgba))<0.4:
        return True
    
blist = []

def findblackl(list1):
    for y in range(H):
        for x in range(W):
            if findblack(list1[y][x]):
                blist.append((x,y))
    return blist


if __name__ == '__main__':
    start = time.time()  # 시작 시간 저장
    img = mpimg.imread('대회/wtf.PNG')
    H,W,waht= (img.shape)
    findblackl(img)
    print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간