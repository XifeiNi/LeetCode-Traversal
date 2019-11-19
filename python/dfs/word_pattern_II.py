class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        return self._isMatch(pattern, str, {}, set())
    def _isMatch(self, pattern, string, char_to_word, used):
        if len(pattern) == 0:
            return len(string) == 0
        char = pattern[0]
        if char in char_to_word:
            word = char_to_word[char]
            if not string.startswith(word):
                return False
            return self._isMatch(pattern[1:], string[len(word):], char_to_word, used)
        
        for i in range(len(string)):
            word = string[:i+1]
            if word in used:
                continue
            used.add(word)
            char_to_word[char] = word
            
            if self._isMatch(pattern[1:], string[len(word):], char_to_word, used):
                return True
            used.remove(word)
            del char_to_word[char]
        return False
