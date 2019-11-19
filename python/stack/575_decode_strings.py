class Solution:
    """
    @param s: an expression includes numbers, letters and brackets
    @return: a string
    """
    def expressionExpand(self, s):
        # write your code here
        stack = []
        for c in s:
            if c != ']':
                stack.append(c)
                continue
            string = []
            while stack and stack[-1] != '[':
                string.append(stack.pop())
            
            # skip the [
            stack.pop()
            repeats = 0
            base = 1
            while stack and stack[-1].isdigit():
                repeats += (ord(stack.pop()) - ord('0')) * base
                base *= 10
            stack.append(''.join(reversed(string))*repeats)
        return ''.join(stack)

