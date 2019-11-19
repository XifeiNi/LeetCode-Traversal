from collections import defaultdict

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0:
            return []
        if len(s) < len(words):
            return []
        result = []
        wsize = len(words[0])
        word_to_frequency = defaultdict(int)
        set_of_words = {}
        for string in words:
            if string not in set_of_words:
                set_of_words[string] = 1
            else:
                set_of_words[string] +=1
        i = 0
        while i < len(s):
            left, right = i, i + len(words)*wsize
            while left < right:
                if s[left:left+wsize] not in set_of_words:
                    break
                if word_to_frequency[s[left:left+wsize]] >= set_of_words[s[left:left+wsize]]:
                    break
                word_to_frequency[s[left:left+wsize]] += 1
                left+=wsize
            word_to_frequency.clear()
            if left >= right:
                
                result.append(i)
            i+=1
        return result
