class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ret = list(s)
        stack = []
        for index, char in enumerate(ret):
            if char == '(' or char == ')':
                if stack and ret[stack[-1]] == '(' and char == ')':
                    stack.pop()
                else:
                    stack.append(index)
        for index in stack:
            ret[index] = ''
        return ''.join(ret)
