# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True :
            rand49 = (rand7() - 1) * 7 + rand7() - 1
            if rand49 <= 39 :
                return rand49 // 4 + 1
        return 0
        
