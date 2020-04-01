class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        index, remain = 0, 0
        for i in range(len(gas)):
            remain = remain + gas[i] - cost[i]
            if remain < 0:
                remain = 0
                index = i + 1
        return index
