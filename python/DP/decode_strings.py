class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
                continue
            string = []
            while stack and stack[-1] != '[':
                string.append(stack.pop())
            
            # pop [
            stack.pop()
            
            # find the number
            base = 1
            repeats = 0
            while stack and stack[-1].isdigit():
                repeats += (ord(stack[-1]) - ord('0'))*base 
                base = base*10
                stack.pop()
            stack.append(''.join(reversed(string)) *repeats)
        return ''.join(stack)
