"""
This function takes the root of the binary tree as input and returns True if the binary tree is complete and False
otherwise.
The function uses a level-order traversal approach and a boolean variable is_full to check if the binary tree is
complete or not.
If a node has a left child but no right child, or if a node has a missing left child but has a right child, the function
 returns False as the binary tree is not complete.
Otherwise, the function returns True as the binary tree is complete.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def is_complete_tree(root):
    if root is None:
        return True
    queue = [root]
    is_full = True
    while queue:
        node = queue.pop(0)
        if node.left:
            if not is_full:
                return False
            queue.append(node.left)
        else:
            is_full = False
        if node.right:
            if not is_full:
                return False
            queue.append(node.right)
        else:
            is_full = False
    return True
root=TreeNode(1)
root.left=TreeNode(2)
root.right=TreeNode(3)
# root.left.left=TreeNode(4)
# root.left.right=TreeNode(5)
root.right.left=TreeNode(6)
root.right.right=TreeNode(5)
print(is_complete_tree(root))





