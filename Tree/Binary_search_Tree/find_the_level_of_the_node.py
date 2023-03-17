class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_level(root, node, level=0):
    if root is None:
        return -1
    if root == node:
        return level
    left_level = find_level(root.left, node, level+1)
    if left_level != -1:
        return left_level
    right_level = find_level(root.right, node, level+1)
    if right_level != -1:
        return right_level
    return -1
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

node = root.left.right
level = find_level(root, node)
print("Level of node", node.value, "is", level)
