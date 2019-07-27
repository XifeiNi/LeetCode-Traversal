class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique charcacter in a given string
    """
    def firstUniqChar(self, str):
        hashMap = {}
        for c in str:
            hashMap[c] = hashMap.get(c, 0) + 1
        for c in str:
            if hashMap[c] == 1:
                return c
