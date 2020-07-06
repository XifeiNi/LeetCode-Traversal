class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key = lambda x: (-len(x), x))
        for word in d:
            if self.isSubsequence(s, word):
                return word
        return ""
    def isSubsequence(self, string, word):
        if len(string) < len(word):
            return False
        index = 0
        for char in string:
            if index == len(word):
                break
            if char == word[index]:
                index += 1
        return index == len(word)
