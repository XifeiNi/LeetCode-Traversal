class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num2) - 1
        multi = 1
        ret = 0
        while i >= 0:
            ret = self.plus(str(ret), str(multi*int(num2[i])*int(num1)))
            multi = multi*10
            i-=1
        return ret
    def plus(self, num1, num2):
        ret = []
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        while i >= 0 and j >= 0:
            if int(num1[i]) + int(num2[j]) + carry >= 10:
                ret.append(str((int(num1[i]) + int(num2[j]) + carry)%10))
                carry = 1
            else:
                ret.append(str((int(num1[i]) + int(num2[j]) + carry)%10))
                carry = 0
            
            i-=1
            j-=1
        while i >= 0:
            if int(num1[i])  + carry >= 10:
                ret.append(str((int(num1[i]) + carry)%10))
                carry = 1
            else:
                ret.append(str((int(num1[i]) + carry)%10))
                carry = 0
            i-=1
        while j >= 0:
            if int(num2[j])  + carry >= 10:
                ret.append(str((int(num2[j]) + carry)%10))
                carry = 1
            else:
                ret.append(str((int(num2[j]) + carry)%10))
                carry = 0
            j-=1
        if carry > 0:
            ret.append(str(carry))
        
        #print(ret)
        return ''.join(reversed(ret))
        
