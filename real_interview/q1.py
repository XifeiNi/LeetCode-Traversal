array1 = input()
array = []
for i in range(len(array1)):
	if array1[i] == ' ':
		array.append(array1[:i])
		array.append(array1[i+1:])
firstSum = 0
for num in list(array[0]):
	firstSum+=int(num)
secondSum = 0
for num in list(array[1]):
	secondSum+=int(num)
print(firstSum%secondSum)