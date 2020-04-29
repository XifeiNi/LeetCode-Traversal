
from collections import deque

def readIn():
    sizeOfTest = int(input())
    i = 0
    input_arr = []
    while i < sizeOfTest:
        input_arr.append([])
        ToBeRead = int(input())
        for j in range(ToBeRead):
            input_arr[i].append(input())
       	i += 1
    output(input_arr)

def output(processed):
	for i in range(len(processed)):
		queue = deque([])
		for string in processed[i]:
			if string.startswith("PUSH"):
				add, num = string.split()
				queue.append(int(num))
			if string == "TOP":
				if len(queue) == 0:
					print("-1")
				else:
					print(queue[0])
			if string == "POP":
				if len(queue) == 0:
					print("-1")
				else:
					queue.popleft()
			if string == "CLEAR":
				queue = []
			if string == "SIZE":
				print(len(queue))


readIn()
