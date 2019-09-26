from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for string in strs:
            sorted_word = ''.join(sorted(list(string)))
            anagram_dict[sorted_word].append(string)
        return anagram_dict.values()
        
