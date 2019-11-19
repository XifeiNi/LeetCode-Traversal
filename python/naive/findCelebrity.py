# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        celeb = 0
        for i in range(n):
            if knows(celeb, i):
                celeb = i
        for i in range(n):
            if knows(celeb, i) and i != celeb:
                return -1
            if not knows(i, celeb) and i != celeb:
                return -1
        return celeb
