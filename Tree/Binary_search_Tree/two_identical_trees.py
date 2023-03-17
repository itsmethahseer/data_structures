class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def isIdentical(root1: TreeNode, root2: TreeNode) -> bool:
    if root1 is None and root2 is None:
        return True
    if root1 is not None and root2 is not None:
        return (root1.val == root2.val and
                isIdentical(root1.left, root2.left) and
                isIdentical(root1.right, root2.right))
    return False

root1=TreeNode(1)
root2=TreeNode(1)
root1.left=TreeNode(3)
root2.left=TreeNode(3)
root1.right=TreeNode(4)
root2.right=TreeNode(4)
print(isIdentical(root1,root2))




