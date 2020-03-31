class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s.reverse()

        index = 0
        for i in range(len(s)):
            if s[i] == " ":
                s[index: i] = reversed(s[index: i])
                index = i + 1

        s[index: ] = reversed(s[index: ])

