class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator%denominator == 0:
            return str(numerator//denominator)
        res = ""
        sign = "-" if numerator * denominator < 0 else ""
        
        numerator, denominator = abs(numerator), abs(denominator)
        integer = str(numerator//denominator)
        rem = numerator%denominator
        res = sign + integer + "."
        num_to_pos = {}
        while rem!= 0:
            if rem in num_to_pos:
                break
            num_to_pos[rem] = len(res)
            n, rem = divmod(10*rem, denominator)
            res += str(n)
        
        if rem  in num_to_pos:
            index = num_to_pos[rem]
            res = res[:index] + '(' + res[index:] + ')'
        return res
