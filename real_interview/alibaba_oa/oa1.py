def readIn():
	testCases = int(input())

	for i in range(testCases):
		people = map(int, input().strip().split())
		ppl_arr = []
		ppl_arr.extend(people)
		fruit = map(int, input().strip().split())
		fruit_arr = []
		fruit_arr.extend(fruit)
		maxFruit(ppl_arr[1], fruit_arr)

def maxFruit(people, fruit):
	minFruit = min(fruit)
	if sum(fruit) < people:
		print("0")
		return
	ret = max(fruit)
	overall = sum(fruit)
	while not canSplit(ret, fruit, people):
		ret -= 1
	if ret < 0:
		print("0")
		return
	print(ret)
	return
def canSplit(ret, fruits, people):
	split = 0
	for fruit in fruits:
		div = fruit // ret
		split += div
	return split >= people
readIn()

