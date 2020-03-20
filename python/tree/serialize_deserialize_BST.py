# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return '{}'
        result = [root.val]
        queue = [root]
        
        while queue:
            newNode = []
            for node in queue:
                if node.left:
                    newNode.append(node.left)
                    result.append(node.left.val)
                else:
                    result.append("#")
                if node.right:
                    newNode.append(node.right)
                    result.append(node.right.val)
                else:
                    result.append("#")
            queue = newNode
        while result and result[-1] == "#":
            result.pop()
        return '{' + ','.join(map(str, result)) + '}'
            
        

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        if data == '{}':
            return None
        nodes = deque([TreeNode(n) for n in data[1:-1].split(',')])
        root = nodes.popleft()
        p = [root]
        while p:
            new_p = []
            for n in p:
                if nodes:
                    left = nodes.popleft()
                    if left.val == "#":
                        n.left = None
                    else:
                        n.left = left
                        new_p.append(left)
                if nodes:
                    right = nodes.popleft()
                    if right.val == "#":
                        n.right = None
                    else:
                        n.right = right
                        new_p.append(right)
                p = new_p
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
