from collections import deque
def readIn():
	size = int(input())
	arr = []
	for _ in range(size):
		arr.append(input())
	process(arr)

def process(arr):
	queue = deque([])
	for string in arr:
		if string.startswith("add"):
			add, num = string.split()
			queue.append(int(num))
		if string == "peek":
			print(queue[0])
		if string == "poll":
			queue.popleft()
readIn()
