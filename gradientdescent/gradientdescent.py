import numpy as np
import matplotlib.pyplot as plt

function = lambda x: (x ** 3)-(3 *(x ** 2))+7

#Get 1000 evenly spaced numbers between -1 and 3 (arbitratil chosen to ensure steep curve)
x = np.linspace(-1,3,500)

#Plot the curve
plt.plot(x, function(x))
plt.show()

def deriv(x):
	x_deriv = 3* (x**2) - (6 * (x))
	return x_deriv

def step(x_new, x_prev, precision, l_r):
	x_list, y_list = [x_new], [function(x_new)]
	while abs(x_new - x_prev) > precision:
		x_prev = x_new
		d_x = - deriv(x_prev)
		x_new = x_prev + (l_r * d_x)
		x_list.append(x_new)
		y_list.append(function(x_new))
	print ("Local minimum occurs at: "+ str(x_new))
	print ("Number of steps: " + str(len(x_list)))

	plt.subplot(1,2,2)
	plt.scatter(x_list,y_list,c="g")
	plt.plot(x_list,y_list,c="g")
	plt.plot(x,function(x), c="r")
	plt.title("Gradient descent")

	plt.subplot(1,2,1)
	plt.scatter(x_list,y_list,c="g")
	plt.plot(x_list,y_list,c="g")
	plt.plot(x,function(x), c="r")
	plt.xlim([1.0,2.1])
	plt.title("Zoomed in Gradient descent to Key Area")
	plt.show()

step(0.5, 0, 0.001, 0.05)