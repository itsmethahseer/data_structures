class Node:
    def __init__(self, data, left=None, right=None):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        current_node = self.root
        if current_node is None:
            self.root = Node(data)
            return
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = Node(data)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = Node(data)
                    break
                else:
                    current_node = current_node.right

    def contains(self, data):
        current_node = self.root
        while current_node is not None:
            if data < current_node.data:
                current_node = current_node.left
            elif data > current_node.data:
                current_node = current_node.right
            else:
                return True
        return False










    def remove(self, data):
        self.remove_helper(data, self.root, parent_node=None)

    def remove_helper(self, data, current_node, parent_node):
        while current_node is not None:
            if data < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            elif data > current_node.data:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.data = self.get_min_value(current_node.right)
                    self.remove_helper(current_node.data, current_node.right, current_node)
                else:
                    if parent_node is None:
                        if current_node.right is None:
                            self.root = current_node.left
                        else:
                            self.root = current_node.right
                    else:
                        if parent_node.left == current_node:
                            if current_node.right is None:
                                parent_node.left = current_node.left
                            else:
                                parent_node.left = current_node.right
                        else:
                            if current_node.right is None:
                                parent_node.right = current_node.left
                            else:
                                parent_node.right = current_node.right
                break

    def get_min_value(self, current_node):
        if current_node.left is None:
            return current_node.data
        else:
            return self.get_min_value(current_node.left)

    def get_max_value(self, current_node):
        if current_node.right is None:
            return current_node.data
        else:
            return self.get_min_value(current_node.right)

    def in_order(self):
        self.in_order_helper(self.root)

    def in_order_helper(self, node):
        if node is not None:
            self.in_order_helper(node.left)
            print(node.data, end=" ")
            self.in_order_helper(node.right)

    def pre_order(self):
        self.pre_order_helper(self.root)

    def pre_order_helper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.pre_order_helper(node.left)
            self.pre_order_helper(node.right)

    def post_order(self):
        self.post_order_helper(self.root)

    def post_order_helper(self, node):
        if node is not None:
            self.post_order_helper(node.left)
            self.post_order_helper(node.right)
            print(node.data, end=" ")
    def find_closest(self, target):
        current_node = self.root
        closest = current_node.data
        while current_node is not None:
            if abs(target - closest) > abs(target - current_node.data):
                closest = current_node.data
            if target < current_node.data:
                current_node = current_node.left
            elif target > current_node.data:
                current_node = current_node.right
            else:
                break
        return closest

    def validate_bst(self, tree):  # O(n)T , O(d)S
        return self.validate_bst_helper(tree, float('-inf'), float('inf'))

    def validate_bst_helper(self, tree, min_value, max_value):
        if tree is None:
            return True
        if tree.data < min_value or tree.data >= max_value:
            return False
        is_left_valid = self.validate_bst_helper(tree.left, min_value, tree.data)
        return is_left_valid and self.validate_bst_helper(tree.right, tree.data, max_value)


tree = BinarySearchTree()
tree.insert(10)
tree.insert(8)
tree.insert(4)
tree.insert(9)
tree.insert(11)
# print("in order traversal")
# tree.remove(4)
# tree.in_order()
# print("in order traversal")
# tree.pre_order()
# print("pre order traversal")
# tree.post_order()
# print("post order traversal")
# print(tree.find_closest(12))
