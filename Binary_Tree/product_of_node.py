#Find the product of all nodes in a Binary Tree.

class Node:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left = Node(8)


def product_of_nodes(root):
    if root is None:
        return 1
    return root.val * product_of_nodes(root.left) * product_of_nodes(root.right)

print(product_of_nodes(root))