#Q2. Find the minimum value in a Binary tree


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


def min_value_in_binary_tree(root):
    if root is None:
        return float('inf')
    
    min_left = min_value_in_binary_tree(root.left)
    min_right = min_value_in_binary_tree(root.right)

    return min(root.val ,min_left,min_right)
    

print(min_value_in_binary_tree(root))