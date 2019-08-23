class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for i in range(len(nums) - 2, -1, -1):
            print(i)
            if nums[i] < nums[i+1]:
                index = i
                break
        else:
            nums.reverse()
            return
        for j in range(len(nums) - 1, index, -1):
            if nums[j] > nums[index]:

                nums[j], nums[index] = nums[index], nums[j]
                break
        #print(index)
        # reverse
        start, end = index+1, len(nums) - 1
        while start < end:
            #print("j")
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end-=1
        
