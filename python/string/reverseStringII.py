class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        answer = ""
        for i in range(0, len(s), 2*k):
            for j in range(min(len(s) - 1, i + k - 1), i - 1, -1):
                answer = answer + s[j]
            for q in range(i + k, min(len(s), i + 2*k)):
                answer = answer + s[q]
        return answer
            
            
