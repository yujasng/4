import numpy as np
import matplotlib.pyplot as plt
	
def fit_line(blacklist):
	num_a = 0
	den_a = 0
	x_bar = 0
	y_bar = 0
	n = len(blacklist)
	
	for i in range(len(blacklist)):
		x,y = blacklist[i]
		x_bar += x
		y_bar += y
		
	x_bar /= n 
	y_bar /= n
	
	for i in range(len(blacklist)):
		num_a += (x - x_bar) * (y - y_bar)
		den_a += (x - x_bar)**2
		
	
	a = num_a / den_a
	b = y_bar - a * x_bar
		
	return a,b
	
image = np.loadtxt("line.csv", delimiter=",")
image = image.astype(int)

blacklist = []
for y in range(image.shape[0]):
	for x in range(image.shape[1]):
		if image[y,x] == 0:
			print("(%d,%d)" %(x,y))
			blacklist.append((x,y))
	
	
a,b = fit_line(blacklist)
			
print(a,b)


			
x = np.linspace(0,8,9)
y = a*x+b
plt.plot(x,y, 'r-', linewidth = 4)
plt.imshow(image,cmap='gray', interpolation ='nearest')
plt.show()


