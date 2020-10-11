def maxSum1DArray(array):
	max_so_far, max_ending_here = 0, 0
	for element in array:
		max_ending_here = max(max_ending_here, element)
		max_so_far = max(max_ending_here, max_so_far)
	return max_so_far
def maxSum2DArray(matrix):
	maxSum = 0
	for left in range(maxLength(matrix)):
		right = left
		while right < maxLength(matrix):
			sumArray = []
			initialTemp = []
			for i in range(len(matrix)):
				if len(matrix[i]) < right:
					sumArray.append(initialTemp)
					initialTemp = []
				else:
					initialTemp.append(matrix[i][right])
			for sum in sumArray:
				maxSum = max(maxSum, maxSum1DArray(sum))
	return maxSum

def maxLength(matrix):
	maximum = 0
	for array in matrix:
		maximum = max(len(array, maximum))
	
	return maximum
