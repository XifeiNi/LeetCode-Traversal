class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True
        xVals = [point[0] for point in points]
        axis = (max(xVals) + min(xVals)) / 2
        counts = collections.defaultdict(int)
        
        pt_set = set()
        for x, y in points:
            pt_set.add((x, y))
        
        for x, y in list(pt_set):
            if x == axis:
                continue
            
            counts[(x, y)] += 1
        for (x, y) in counts:
            x_ = axis * 2 - x
            if (x_, y) not in counts or counts[(x, y)] != counts[(x_, y)]:
                return False
                
        return True
