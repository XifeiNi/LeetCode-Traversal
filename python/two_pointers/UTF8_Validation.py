class Solution(object):
    def checkSum(self, start, increment, nums):
        for i in range(start + 1, increment + start + 1):
            if i >= len(nums):
                return False
            if (nums[i] >> 6) != 0b10:
                return False
        return True
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and self.checkSum(start, 3, data):
                start += 4
            elif (first >> 4) == 0b1110 and self.checkSum(start, 2, data):
                start += 3
            elif (first >> 5) == 0b110 and self.checkSum(start, 1, data):
                start += 2
            elif first >> 7 == 0:
                start += 1
            else:
                return False
        return True
