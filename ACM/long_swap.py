def isSorted(string):
	for i in range(len(string) - 1):
		if string[i] > string[i + 1]:
			return False
	return True
def longSwap():
	g = input()
	input_list = g.split()
	string = input_list[0]
	k = input_list[1]
	if isSorted(string):
		print("Yes")
		return
	if int(k) <= len(string)//2:
		print("Yes")
		return
	else:
		print("No")
		return
	
longSwap()
