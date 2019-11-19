class Solution(object):
    def pourWater(self, heights, V, K):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        N = len(heights)
        for i in range(V):
            position = K
            for j in range(K + 1, N):
                if heights[j] < heights[j-1]:
                    position = j
                elif heights[j] > heights[j-1]:
                    break
            for q in range(K - 1, -1, -1):
                if heights[q] < heights[q+1]:
                    position = q
                elif heights[q] > heights[q+1]:
                    break
            heights[position]+=1
        return heights
        
