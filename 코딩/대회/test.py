import time
import numpy as np
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
import cv2
from PIL import Image
from glob import glob

def black_decision(hueval):
    if hueval[2] <= 0.3:
        return 'black'

def dfs(x,y,Image):
    stack =[]
    line = []
    stack.append((x,y))
    while stack:
        cx, cy = stack.pop()
        if black_decision(Image) == 'black' and buffer[cy][cx] == 0:
            line.append((cx, cy))
            buffer[cy][cx] = 1
            for dx, dy in [(1, 0), (1, 1), (1, -1), (-1,-1), (-1, 1), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = cx + dx, cy + dy
                if 0<=nx<W and 0<=ny<H and black_decision(img[ny][nx]) == 'black' and buffer[ny][nx] == 0:
                    stack.append((nx, ny))
                else:
                    pass
    return line

def find_monitor(image):
    max_line = []
    #TODO_3
    for x in wlist:
        for y in range(H):
            if black_decision(image[y][x]) == 'black' and buffer[y][x] == 0:
                line = dfs(x, y, image[y][x])
                if len(line) > len(max_line):
                    max_line = line
    return max_line

def find_color(blacklist):
    blacklist.sort(key = lambda x:x[1])
    klist = []
    for i in range(len(blacklist)-1):
        delta = blacklist[i+1][0]-blacklist[i][0]
        if delta != 1 and delta >0:
            for j in range(delta-1):
                color_decision(img[blacklist[i][1]][blacklist[i][0]+j][0],img[blacklist[i][1]][blacklist[i][0]+j][1],img[blacklist[i][1]][blacklist[i][0]+j][2])
    answer = {'R':redcount,'G':greencount,'B':bluecount}
    return max(answer,key=answer.get)

def color_decision(hue,saturation,value):
    global bluecount,redcount,greencount
    if 340<hue or hue<20 and saturation >0.5 and value> 0.5:
        redcount += 1
    elif 100<hue<140 and saturation >0.5 and value> 0.5:
        greencount += 1
    elif 220<hue<260 and saturation >0.5 and value> 0.5:
        bluecount += 1
    else:
        pass

def find_monitor2(image):
  global path
  blacklist =[[],[],[],[]]
  counter_for_monitor=0
  for x in wlist:
    for y in range(H):
      if black_decision(image[y][x]) == 'black':
        counter_for_monitor+=1
        blacklist[0].append((x,y))
        if counter_for_monitor > 1:
          if abs(blacklist[0][-1][1]-blacklist[0][-2][1])>75:
            path = 1
            return find_monitor(image)
        break
  counter_for_monitor=0
  for x in wlist:
    for y in range(H):
      if black_decision(image[H-y-1][x]) == 'black':
        counter_for_monitor+=1
        blacklist[1].append((x,H-y-1))
        if counter_for_monitor > 1:
          if abs(blacklist[1][-1][1]-blacklist[1][-2][1])>75:
            path = 1
            return find_monitor(image)
        break
  counter_for_monitor=0
  for y in hlist:
    for x in range(W):
      if black_decision(image[y][W-x-1]) == 'black':
        counter_for_monitor+=1
        blacklist[2].append((W-x-1,y))
        if counter_for_monitor > 1:
          if abs(blacklist[2][-1][0]-blacklist[2][-2][0])>75:
            path = 1
            return find_monitor(image)
        break
  counter_for_monitor=0
  for y in hlist:
    for x in range(W):
      if black_decision(image[y][x]) == 'black':
        counter_for_monitor+=1
        blacklist[3].append((x,y))
        if counter_for_monitor > 1:
          if abs(blacklist[3][-1][0]-blacklist[3][-2][0])>75:
            path = 1
            return find_monitor(image)
        break
  return blacklist

def scattered_test(list_):
  for i in range(len(list_[0])):
    for j in range(list_[1][i][1]-list_[0][i][1]):
      color_decision(img[list_[1][i][1]-j][list_[1][i][0]][0],img[list_[1][i][1]-j][list_[1][i][0]][1],img[list_[1][i][1]-j][list_[1][i][0]][2])
  answer = {'R':redcount,'G':greencount,'B':bluecount}
  return max(answer,key=answer.get)


def color_detector(filename):
    #TODo
    L = find_monitor2(img)
    if path == 1:
        print(find_color(L))
    else:
        print(scattered_test(L))

    return # 'R' or 'G' or 'B'
    
if __name__ == '__main__':
    wlist = []
    hlist = []
    result=[]
    path = 0
    redcount =0
    greencount=0
    bluecount=0
    for filename in sorted(glob('public_imgs/*.PNG')): 
        img = mpimg.imread(filename)
        img = cv2.resize(img,(0,0), fx = 0.4, fy = 0.4, interpolation = cv2.INTER_AREA)
        img = cv2.cvtColor(img,cv2.COLOR_RGB2HSV)
        H,W,waht= (img.shape)
        wlist = [int((x+1)*W/64) for x in range(63)]
        hlist = [int((x+1)*H/64) for x in range(63)]
        buffer = np.zeros([H,W])
        result.append(color_detector(img))
    print(result)