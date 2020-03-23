# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        self.traverse(root, result)
        return result
    def traverse(self, root, result):
        if root is None:
            return
        result.append(root.val)
        self.traverse(root.left, result)
        self.traverse(root.right, result)
