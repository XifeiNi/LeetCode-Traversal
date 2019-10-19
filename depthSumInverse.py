
class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        from collections import deque
        queue = deque(nestedList)
        sum_list = []
        while queue:
            n = len(queue)
            level_sum = 0
            for i in range(n):
                element = queue.popleft()
                if element.isInteger():
                    level_sum += element.getInteger()
                else:
                    
                    queue.extend(element.getList())
            sum_list.append(level_sum)
        max_depth = len(sum_list)
        ret = 0
        for i, level in enumerate(sum_list):
            depth = max_depth - i
            ret += depth*level
        return ret
