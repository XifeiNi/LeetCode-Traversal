DELTA = [(1, 1), (1, -1), (1, 0)]
matrix = [[9, 10, 15, 12, 11], [7, 5, 11, 6, 8], [4, 1, 27, 13, 17], [2, 4, 18, 2, 1], [15, 3, 22, 6, 10], [8, 2, 5, 9, 6]]

def readIn():
	row, col = map(int, input().strip().split())
	data = map(int, input().strip().split())
	data2 = []
	data2.extend(data)
	matrix = [[0 for _ in range(col)] for _ in range(row)]
	for i in range(row):
		for j in range(col):
			matrix[i][j] = data2[i * col + j]
	print(getTwoRobots(matrix))

def findAllPaths(maze, curPath, allPaths, startX, startY, endX, endY):
	#print(startX, startY)
	if endY == startY and endX == startX:
		
		allPaths.append(list(curPath))
		return
	for deltaX, deltaY in DELTA:
		if (startX + deltaX, startY + deltaY) in curPath:
			continue
		if 0 <= startX + deltaX < len(maze) and 0 <= startY + deltaY < len(maze[0]):
			curPath.append((startX + deltaX, startY + deltaY))
			findAllPaths(maze, curPath, allPaths, startX + deltaX, startY + deltaY, endX, endY)
			curPath.pop()
	return

def getTwoRobots(maze):
	allPaths1, allPaths2 = [], []
	
	findAllPaths(maze, [], allPaths1, 0, 0, len(maze) - 1, 0)
	findAllPaths(maze, [], allPaths2, 0, len(maze[0]) - 1, len(maze) - 1, len(maze[0]) - 1)
	ret = 0
	for path1 in allPaths1:
		for path2 in allPaths2:
			ret = max(ret, getCoins(path1, path2, maze))
	return ret + maze[0][0] + maze[0][len(maze[0]) - 1]
	

def getCoins(path1, path2, maze):
	allPts = set(path1).union(set(path2))
	coins = 0
	for x, y in list(allPts):
		coins += maze[x][y]
	return coins
readIn()

