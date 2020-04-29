import math
def height(num):
	h = 1
	nodeNum = 1
	while nodeNum < num:
		nodeNum = math.pow(2, h) - 1
		h += 1
	return h
def getAnt(num, k):
	nodesInK = math.pow(2, k - 1)
	height = height(num)
	nodesInNum = math.pow(2, height - 1)
	