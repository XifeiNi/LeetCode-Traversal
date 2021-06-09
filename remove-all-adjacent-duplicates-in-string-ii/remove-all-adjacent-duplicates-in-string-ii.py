class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [["#", 0]]
        for char in s:
            if stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return ''.join(char * k for char, k in stack[1:])