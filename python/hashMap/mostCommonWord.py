from collections import defaultdict
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ')
        wordList = paragraph.split()
        bannedWord = set()
        for word in banned:
            bannedWord.add(word)
        freq = defaultdict(int)
        for word in wordList:
            if not word[-1].isalpha():
                word = word[:-1]
            if word.lower() not in bannedWord:
                freq[word.lower()] += 1
        return max(freq, key=freq.get)
