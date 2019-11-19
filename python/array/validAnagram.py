from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_map = defaultdict(int)
        t_map = defaultdict(int)
        for i in range(len(s)):
            s_map[s[i]]+=1
            t_map[t[i]]+=1
        for key in t_map:
            if s_map[key] != t_map[key]:
                return False
        return True
