class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return "0"
        stack, num, sign = [], 0, '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')

            if (not s[i].isspace() and not s[i].isdigit()) or i == len(s) - 1:
                if sign == '+':
                    stack.append(num)
                if sign == '-':
                    stack.append(-num)
                if sign == '*':
                    stack.append(stack.pop()*num)
                if sign == '/':
                    tmp = stack.pop()
                    if tmp// num < 0 and tmp%num != 0:
                        stack.append(tmp//num + 1)
                    else:
                        stack.append(tmp//num)
                sign = s[i]
                num = 0

        return sum(stack)
