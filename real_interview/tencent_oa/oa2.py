import math
def readIn():
	sizeOfTest = int(input())
	i = 0
	input_arr = []
	while i < sizeOfTest:
		sizeOfSet = int(input())
		A, B = [], []
		for _ in range(sizeOfSet):
			x, y = map(int, input().strip().split())
			A.append((x, y))
		for _ in range(sizeOfSet):
			x, y = map(int, input().strip().split())
			B.append((x, y))
		input_arr.append(A)
		input_arr.append(B)
		i += 1
	output(input_arr)

def output(input_arr):
	i = 0
	while i < len(input_arr):
		getSmallest(input_arr[i], input_arr[i + 1])
		i += 2

def getSmallest(arr1, arr2):
	ret = 1000000
	for num1 in arr1:
		for num2 in arr2:
			ret = min(ret, (math.sqrt((num1[0] - num2[0]) * (num1[0] - num2[0]) + (num1[1] - num2[1]) * (num1[1] - num2[1]))))
			if ret == 0:
				print("0.000")
				return
	print("%.3f" % ret)
readIn()
