# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        results = []
        self.dfs(root, sum, [], results)
        return results
    
    def dfs(self, root, target, permutation, results):
        if not root:
            return

        if not root.left and not root.right and root.val == target:
            results.append(list(permutation + [root.val]))
            return
        permutation.append(root.val)
        self.dfs(root.left, target - root.val, permutation, results)
        self.dfs(root.right, target - root.val, permutation, results)
        permutation.pop()
