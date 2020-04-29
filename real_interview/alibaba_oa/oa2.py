from collections import defaultdict
def readIn():
	niu, num_Candy = map(int, input().split())
	candies = map(int, input().split())
	candy_arr = []
	candy_arr.extend(candies)
	pairs = defaultdict(int)
	k = int(input())
	for i in range(k):
		i, j = map(int, input().split())
		pairs[i] = j
		pairs[j] = i
	niu_array = []
	candy_consume = []
	for i in range(1, niu + 1):
		if pairs[i] == -1:
			continue
		if pairs[i] == 0:
			niu_array.append(1)
			candy_consume.append(candy_arr[i - 1])
		else:

			niu_array.append(2)
			candy_consume.append(candy_arr[i - 1] + candy_arr[pairs[i] - 1])
			pairs[pairs[i]] = -1
	toBeSorted = []
	for i in range(len(niu_array)):
		toBeSorted.append((-niu_array[i], candy_consume[i]))
	toBeSorted.sort()
	max_niu = 0
	candy = 0
	for ppl, can in toBeSorted:
		candy += can
		if candy > num_Candy:
			break
		max_niu += ppl
	print(-max_niu)
readIn()


