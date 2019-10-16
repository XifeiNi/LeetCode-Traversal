class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        to_be_reversed = s.split()
        return ' '.join(reversed(to_be_reversed))
