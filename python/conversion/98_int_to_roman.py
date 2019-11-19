class Solution:
    """
    @param n: The integer
    @return: Roman representation
    """
    def intToRoman(self, n):
        one = ['',"I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        ten = ['',"X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        hundred = ['', "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        thousand = ['',"M", "MM", "MMM"]
        
        total = [one, ten, hundred, thousand]
        
        result = []
        count = 0
        while n > 0:
            end_digit = n%10
            result.append(total[count][end_digit])
            n = n//10
            count+=1
        result.reverse()
        return ''.join(result)
