import math
import csv
import operator
import sys
from string import split


def maxNum(a, b):
	if a > b:
		return a
	return b

def minNum(a, b):
	if a > b:
		return b
	return a

def hypot(a, b):
	ans = a*a + b*b
	ans = math.sqrt(ans)
	return ans

string = "abcdefghijklmnopqrstuvwxyz"
fileList = list(string)

for fileName in fileList:
	result=[]
	name = fileName + ".txt"
	with open(name,'r') as f:
		for line in f:
			result.append(map(long,line[:-3].split(',')))

	x_min = minNum(result[0][0], result[-1][0]) 
	y_min = minNum(result[0][1], result[-1][1])
	x_max = maxNum(result[0][0], result[-1][0]) 
	y_max = maxNum(result[0][1], result[-1][1])
	# print result
	f8 = 0
	f9 = 0
	f10 = 0
	f11 = 0
	f12 = 0
	prev = result[0]
	old_delta_x = prev[0]
	old_delta_y = prev[1]
	
	for point in result[1:]:
		if point[2] == prev[2]:
			continue
		x_min = minNum(x_min, point[0])
		x_max = maxNum(x_max, point[0])
		y_min = minNum(y_min, point[1])
		y_max = maxNum(y_max, point[1])

		delta_x = point[0] - prev[0]
		delta_y = point[1] - prev[1]
		f8 += hypot(delta_x, delta_y)
		rotation = 0
		if delta_x != 0 and old_delta_x != 0:
			rotation = math.atan(float(delta_y) / delta_x) - math.atan(float(old_delta_y) / old_delta_x)
		
		dividen = float(delta_x * old_delta_y - old_delta_x * delta_y)
		divid = (delta_x * old_delta_x + delta_y * old_delta_y)
		if divid != 0:
			rotation = dividen / divid
		else:
			if dividen > 0:
				rotation = 1.57
			else:
				rotation = -1.57
		
		f9 += rotation
		f10 += abs(rotation)
		f11 += rotation ** 2
		f12 = maxNum(f12, (hypot(delta_x, delta_y)/(point[2] - prev[2]))**2)
		prev = point
		old_delta_y = delta_y
		old_delta_x = delta_x

	case = []
	case.append(fileName)
	d_start = hypot(result[2][1] - result[0][1], result[2][0] - result[0][0])
	f1 = (result[2][0] - result[0][0]) / d_start
	case.append(f1);
	f2 = (result[2][1] - result[0][1]) / d_start
	case.append(f2)
	f3 = hypot(y_max - y_min, x_max - x_min)
	case.append(f3)
	f4 = math.asin((y_max - y_min)/f3)
	case.append(f4)
	f5 = hypot(result[-1][0] - result[0][0], result[-1][1] - result[0][1])
	case.append(f5)
	f6 = (result[-1][0] - result[0][0]) / f5
	case.append(f6)
	f7 = (result[-1][1] - result[0][1]) / f5
	case.append(f7)
	case.append(f8)
	case.append(f9)
	case.append(f10)
	case.append(f11)
	case.append(f12)
	f13 = result[-1][2] - result[0][2]
	case.append(f13)

	csvfile = file('csv_test.csv', 'a+')
	writer = csv.writer(csvfile)
	writer.writerow(case)
	csvfile.close()




	