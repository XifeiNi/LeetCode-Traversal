class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        wordList = str.split(' ')
        char_to_word = {}
        used_words = set()
        if len(wordList) > len(pattern):
            return False
        for i in range(len(pattern)):
            if i >= len(wordList):
                return False
            if pattern[i] not in char_to_word: 
                char_to_word[pattern[i]] = wordList[i]
                if wordList[i] in used_words:
                    return False
                used_words.add(wordList[i])
            if char_to_word[pattern[i]] != wordList[i]:
                return False
        
        return True
