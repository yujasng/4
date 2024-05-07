import numpy as np

def line_point_distance(a, b, x, y):# 점과 직선 사이의 거리 구하기: y=ax+b, (X,Y)
    if type(a) != str:
        distance = (abs(a*x+b-y)/np.sqrt(a**2+1**2))
    else:
        distance = abs(x-b)
        
    return distance


#best line
def fit_line(points_list):
    num_a, den_a, x_bar, y_bar = 0, 0, 0, 0    # a의 분자항, a의 분모항, x값들의 평균, y값들의 평균
    n = len(points_list)

    for i in range(n):   # x_bar & y_bar 계산하기
        x,y = points_list[i]
        x_bar += x
        y_bar += y
    x_bar = x_bar /n
    y_bar = y_bar /n

    for i in range(n):    # num_a & den_a 계산하기
        x,y = points_list[i]
        num_a += (x - x_bar) * (y - y_bar)
        den_a += (x - x_bar) ** 2

    a = num_a / den_a
    b = y_bar - a * x_bar
    return a, b

def RANSAC(image):
    H,W = image.shape
    b_list = []
    iteration = 20
    threshold = 1
    
    for i in range(W):
        for j in range(H):
            if image[j,i] == 0:
                b_list.append((i,j))
                
    n = len(b_list)
    
    max_ = []
    
    for k in range(iteration):
        
        in_line = []
        
        ia,ib = np.random.choice(n,2,False)
        

        
        if b_list[ia][0]-b_list[ib][0] != 0:
            a = (b_list[ia][1]-b_list[ib][1])/(b_list[ia][0]-b_list[ib][0])
            b = (-1)*a*(b_list[ia][0])+b_list[ia][1]
        else:
            a = "undefined"
            b = b_list[ia][0]

        for l in b_list:
            distance = line_point_distance(a,b,l[0],l[1])
            if distance < threshold:
                in_line.append(l)
                
                
        if k == 0:
            max_ = in_line
        elif len(max_) < len(in_line):
            max_ = in_line
    
    
    a1,b1 = fit_line(max_)

    return a1,b1

if __name__ == '__main__':
    image = np.loadtxt("line.csv", delimiter=",")
    a, b = RANSAC(image)
    print(a,b)