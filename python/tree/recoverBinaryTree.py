# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        list_val, list_node = [], []
        self.inorder(root, list_val, list_node)
        list_val.sort()
        for i in range(len(list_val)):
            list_node[i].val = list_val[i]
        return root
    def inorder(self, node, list_val, list_node):
        if not node:
            return
        self.inorder(node.left, list_val, list_node)
        list_val.append(node.val)
        list_node.append(node)
        self.inorder(node.right, list_val, list_node)
