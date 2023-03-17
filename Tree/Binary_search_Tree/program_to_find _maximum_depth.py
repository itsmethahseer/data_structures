# find the maximum depth of a binary tree or maximum length
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def maxDepth(node):
    if node is None:
        return 0
    else:
        # Compute the depth of each subtree
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        # Use the larger one
        if (lDepth > rDepth):
            return lDepth + 1
        else:
            return rDepth + 1
# root = Node(1)
# root.left = Node(2)
# root.right = Node(3)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.left.left=Node(1)
# print(maxDepth(root))