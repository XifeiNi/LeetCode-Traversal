class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        numbers.sort()
        res = []
        length = len(numbers)
        for i in range(0, length-3):
            if i and numbers[i] == numbers[i-1]:
                continue
            for j in range(i+1, length-2):
                if j != i + 1 and numbers[j] == numbers[j-1]:
                    continue
                sum = target - numbers[i] - numbers[j]
                left, right = j + 1, length - 1
                while left < right:
                    if numbers[left] + numbers[right] == sum:
                        res.append([numbers[i], numbers[j], numbers[left], numbers[right]])
                        right-=1
                        left+=1
                        while left < right and numbers[left] == numbers[left-1]:
                            left+=1
                        while left < right and numbers[right] == numbers[right+1]:
                            right-=1
                    elif numbers[left] + numbers[right] > sum:
                        right-=1
                    else:
                        left+=1
        return res
