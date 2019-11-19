ONES = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
        9: "Nine", 10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15: " Fifteen",
        16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
       }
TENS = ["","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
THOUSANDS =  ["","Thousand","Million","Billion"]

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        ret = ""
        for i in range(len(THOUSANDS)):
            if num%1000 != 0:
                ret =  self.hundreds(num%1000) + THOUSANDS[i] + " " + ret
            num//=1000
        return ' '.join(ret.split())
                
                
    def hundreds(self, num):
        ret = ""
        if num//100 != 0:
            ret = ONES[num//100] + " " + "Hundred" + " "
        if num%100 > 19:
            if num%10 == 0:
                ret = ret + TENS[(num%100)//10] + " "
            else:
                ret = ret + TENS[(num%100)//10] + " " + ONES[(num%100)%10] + " "
        elif num%100 != 0 and num%100 <= 19:
            ret = ret + ONES[(num%100)] + " "
        return ret
