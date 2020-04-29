class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def readIn():
    tcase = int(input().strip())
    k = int(intput().strip())
    treeArray = []
    for case in range(tcase):
        data = map(int, input().strip().split())
        treeArray.extend(data)
    tree = deserialize(treeArray)
    return getPairs(tree, k)



def deserialize(data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data[0] == -1:
            return None
        root = TreeNode(data[0])
        queue = [root]
        index = 0
        isLeft = True
        for i in range(1,len(data)):
            if data[i] != -1:
                node = TreeNode(data[i])
                if isLeft == True:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)
            if isLeft is False:
                index+=1
            isLeft = not isLeft
            
                    
        return root

def getPairs(root, k):
    ret = 0
    if root is None:
        return 0
    if root.left is not None and root.right is not None:
        leftCosts, rightCosts = [], []
        toLeaves(root.left, 0, leftCosts)
        toLeaves(root.right, 0, rightCosts)
        ret += getSubPairs(leftCosts, rightCosts, k)
    ret += getPairs(root.left, k) + getPairs(root.right, k)
    return ret

def getSubPairs(leftCosts, rightCosts, k):
    ret = 0
    for left in leftCosts:
        for right in rightCosts:
            if left + right <= k:
                ret += 1
    return ret



def toLeaves(currentNode, cost, allCosts):
    if currentNode is None:
        return
    if currentNode.left is None and currentNode.right is None:
        allCosts.append(cost + 1)
    else:
        toLeaves(currentNode.left, cost + 1, allCosts)
        toLeaves(currentNode.right, cost + 1, allCosts)

print(readIn())
