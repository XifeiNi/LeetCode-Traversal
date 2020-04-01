class Solution:
    def reverseWords(self, s: str) -> str:
        listString = s.split(" ")
        for i in range(len(listString)):
            listString[i] = listString[i][::-1]
        return ' '.join(listString)
