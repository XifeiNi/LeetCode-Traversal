class Solution:
    def calculate(self, s: str) -> int:
        calcPrecedence = {'+' : 0, '-': 0, '*': 1, '/':1}
        stack = []
        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            if char in "+-*/":
                while stack and stack[-1] != '(' and calcPrecedence[stack[-1]] >= calcPrecedence[char]:
                    operation = stack.pop()
                    prevNum = stack.pop()
                    num = self.calc(prevNum, num, operation)
                stack.append(num)
                stack.append(char)
                num = 0
            
            if char == '(':
                stack.append(char)
            if char == ')':
                while stack[-1] != '(':
                    operation = stack.pop()
                    prevNum = stack.pop()
                    num = self.calc(prevNum, num, operation)
                stack.pop()
        while stack:
            operation = stack.pop()
            prevNum = stack.pop()
            num = self.calc(prevNum, num, operation)
        return num
    def calc(self, num1, num2, operation):
        print(num1, num2, operation)
        if operation == '+':
            return num1 + num2
        if operation == '-':
            return num1 - num2
        if operation == '*':
            return num1 * num2
        if operation == '/':
            return num1 // num2
        
            
