from collections import defaultdict
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        point_to_dis = defaultdict(int)
        for i in range(len(points)):
            point_to_dis[(points[i][0], points[i][1])] = points[i][0]*points[i][0] + points[i][1]*points[i][1]
        sorte = list(point_to_dis.keys())
        sorte.sort(key = lambda w: (point_to_dis[w], w))
        ret = []
        for i in range(K):
            ret.append([sorte[i][0], sorte[i][1]])
        return ret
        
            
