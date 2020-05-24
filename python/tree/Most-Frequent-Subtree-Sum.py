# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.subsum = defaultdict(int)
        self.dfs(root)
        largest = 1
        ret = []
        for sub in self.subsum:
            if self.subsum[sub] == largest:
                ret.append(sub)
            elif self.subsum[sub] > largest:
                ret = [sub]
                largest = self.subsum[sub]
        return ret
            
    def dfs(self, node):
        if not node:
            return 0
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        curr_sum = node.val + left + right
        self.subsum[curr_sum] += 1
        return curr_sum
