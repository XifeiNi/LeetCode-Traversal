class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        ans = 0
        stringGroup = self.countGroup(S)
        for word in words:
            wordList = self.countGroup(word)
            if len(wordList) != len(stringGroup):
                continue
            ok = 1
            for i in range(len(stringGroup)):
                if not self.match(wordList[i], stringGroup[i]):
                    ok = 0
                    break
            ans += ok
        return ans
    def countGroup(self, string):
        count = 1
        results = []
        for i in range(1, len(string)):
            if string[i] == string[i - 1]:
                count += 1
            else:
                results.append((string[i - 1], count))
                count = 1
        results.append((string[-1], count))
        return results
    
    def match(self, char1, char2):
        return char1[0] == char2[0] and (char1[1] == char2[1] or (char1[1] < char2[1] and char2[1] >= 3))
