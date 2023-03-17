"""
The above code uses the concept of recursive algorithms to traverse the binary search tree.
There are three types of traversals demonstrated here:

In-order traversal: In this traversal, the left subtree is visited first, then the root, and then the right subtree.
Pre-order traversal: In this traversal, the root is visited first, then the left subtree, and then the right subtree.
Post-order traversal: In this traversal, the left subtree is visited first, then the right subtree, and then the root.
"""
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val)
        in_order_traversal(root.right)
def pre_order_traversal(root):
    if root:
        print(root.val)
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)
def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val)
def insert(root, newValue):
    if root is None:
        root = Node(newValue)
        return root
    if newValue < root.val:
        root.left = insert(root.left, newValue)
    else:
        root.right = insert(root.right, newValue)
    return root
def delete_node(root, key):
    if root is None:
        return root
    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = min_value_node(root.right)
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)
    return root
def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

root=Node(20)
root=insert(root,25)
root=insert(root,18)
delete_node(root,20)
in_order_traversal(root)
