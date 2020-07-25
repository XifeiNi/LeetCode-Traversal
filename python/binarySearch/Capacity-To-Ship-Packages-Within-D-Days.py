class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        left, right = max(weights), sum(weights)
        
        while left  < right:
            mid, days, cur = (left + right) // 2, 1, 0
            for weight in weights:
                if weight + cur > mid:
                    days += 1
                    cur = 0
                cur += weight
            if days > D:
                left = mid + 1
            else:
                right = mid
        current, days = 0, 1
        for weight in weights:
            if weight + current > left:
                days += 1
                current = 0
            current += weight
        if days <= left:
            return left
        else:
            return right
        
