class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack, counter, visited = [], collections.Counter(s), set()
        
        for char in s:
            counter[char] -= 1
            if char in visited:
                continue
            while stack and ord(stack[-1]) > ord(char) and counter[stack[-1]] > 0:
                temp = stack.pop()
                visited.remove(temp)
            stack.append(char)
            visited.add(char)
        return ''.join(stack)
        
