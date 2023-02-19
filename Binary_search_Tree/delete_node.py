"""
This code uses the concept of recursive algorithms to traverse the binary search tree until it finds the node with the specified key.
If the node is found, it deletes it using one of the 3 cases:

If the node has no left child, return its right child.
If the node has no right child, return its left child.
If the node has both left and right children, replace its value with the minimum value in its right subtree and delete that node.
"""




class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

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



