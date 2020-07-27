class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if len(stack) > 0 and stack[-1][0] == char:
                stack[-1][1] += 1
                while len(stack) > 0 and stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        return ''.join(char * freq for char, freq in stack)
