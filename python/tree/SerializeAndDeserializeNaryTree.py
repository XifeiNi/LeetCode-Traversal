"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
SEPERATOR = ','
from collections import deque
class Codec:
    def serialize(self, root: 'Node') -> str:
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if not root:
            return ""
        queue = deque([root])
        res = []
        while queue:
            
            node = queue.popleft()
            if node != SEPERATOR:
                res.append(str(node.val))
                for child in node.children:
                    queue.append(child)
                queue.append(SEPERATOR)
            else:
                res.append(SEPERATOR)
        return "#".join(res)
                
            
            
        
	
    def deserialize(self, data: str) -> 'Node':
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        if not data:
            return None
        nodes = data.split("#")
        root = Node(int(nodes[0]), [])
        queue = deque([root])
        index = 1
        while queue:
            node = queue.popleft()
            while nodes[index] != SEPERATOR:
                new = Node(int(nodes[index]), [])
                node.children.append(new)
                queue.append(new)
                index += 1
            index += 1
        return root
                
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
