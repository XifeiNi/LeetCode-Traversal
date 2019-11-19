class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, check = 0, 0
        for i in range(len(s)):
            
            if s[i] == '(':
                left+=1
                check+=1
            elif s[i] == '*':
                if left > 0:
                    left-=1
                check+=1
            else:
                if left > 0:
                    left -= 1
                check-=1
                if check < 0:
                    return False
        if left > 0:
            return False
        else:
            return True
        
