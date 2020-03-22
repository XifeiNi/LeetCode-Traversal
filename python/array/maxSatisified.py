class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        satisified = 0
        for customer, grump in zip(customers, grumpy):
            if grump == 0:
                satisified += customer
        for i in range(X):
            if grumpy[i] == 1:
                satisified += customers[i]
        ans = satisified
        for i in range(X, len(customers)):
            if grumpy[i - X] == 1:
                satisified -= customers[i - X]
            if grumpy[i] == 1:
                satisified += customers[i]
            
            ans = max(ans, satisified)
        return ans
