import numpy as np

import csv

lnf = open('line.csv', 'r')
img = np.loadtxt('line.csv',delimiter=',')
img = img.astype(int)

coor = [[[i,j,img[i,j],0] for i in range(8)] for j in range(8)]

h,w = img.shape

def checkImage(x,y,image, buffer):

    #TODO_1
    if 0<=x<=h-1 and 0<=y<=w-1 and buffer == 0 and image == 0:
        return True
    else:
        return False
    
    
    
    
k = [-1,0,1]
stack_list = []
def dfs(x,y,image, buffer):
    stack =[]
    line = []
    exist = 1
    def search(x,y):
        coor[y][x][3] = 1
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                try:
                    if checkImage(x+i,y+j,coor[y+j][x+i][2],coor[y+j][x+i][3]):
                        stack.append((x+i,y+j))
                        search(x+i,y+j)
                    else:
                        pass
                except:
                    pass
        return
    stack.append((x,y))
    search(x,y)
    print(stack)
    stack_list.append(stack)

def fit_line(points_list):
    num_a, den_a, x_bar, y_bar = 0, 0, 0, 0
    n = len(points_list)
    for i in range(n):   # x_bar & y_bar 계산하기
        y,x = points_list[i]
        x_bar += x
        y_bar += y

    x_bar = x_bar /n
    y_bar = y_bar /n

    for i in range(n):    # num_a & den_a 계산하기
        y,x = points_list[i]
        num_a += (x - x_bar) * (y - y_bar)
        den_a += (x - x_bar) ** 2

    a = num_a / den_a
    b = y_bar - a * x_bar
    return a, b

for q in range(h):
    for e in range(w):
        if checkImage(e,q,coor[q][e][2],coor[q][e][3]):
            dfs(e,q,coor[q][e][2],coor[q][e][3])


print (stack_list)
lenli = []
for p in range(len(stack_list)):
    lenli.append(len(stack_list[p]))

f = lenli.index(max(lenli))

#no need to change fit_line

if __name__ == '__main__':
    image = np.loadtxt("line.csv", delimiter=",")
    a,b = fit_line(stack_list[f])
    print(a,b)