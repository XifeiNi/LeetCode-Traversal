
class Solution:
    def checkSum(self, data, start, increment):
        for i in range(start+1, start+increment+1):
            if i >= len(data):
                return False
            if (data[i] >> 6) != 0b10:
                return False
        return True
            
    def validUtf8(self, data: List[int]) -> bool:
        start = 0
        while start < len(data):
            first = data[start]
            if (first >> 3) == 0b11110 and self.checkSum(data, start, 3):
                start+=4
            elif (first >> 4) == 0b1110 and self.checkSum(data, start, 2):
                start+=3
            elif (first >> 5) == 0b110 and self.checkSum(data, start, 1):
                start+=2
            elif (first >> 7) == 0:
                start+=1
            else:
                return False
        return True
