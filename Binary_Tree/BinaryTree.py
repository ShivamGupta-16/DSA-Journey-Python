# Defining Node

class Node:
    def __init__(self,value):
        #value, left, right
        self.val = value
        self.left = None
        self.right = None


#example of binary tree

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


def display(root):
    if root is None:
        return None
    print(root.val, end =" ")
    display(root.left)
    display(root.right)

display(root)


#Sum of nodes of binary tree

def sum_of_node(root):
    if root is None:
        return 0
    return root.val + sum_of_node(root.left) + sum_of_node(root.right)

print("\n", sum_of_node(root))


#max value in the tree
def max_of_tree(root):
    if root is None or (root.left is None and root.right is None):
        return root
    
    max_left = max_of_tree(root.left)
    max_right = max_of_tree(root.right)

    return max(max_left,max_right, root, key = lambda x: x.val if x else float('-inf'))

print(max_of_tree(root).val)

#Height of the tree
def find_height(root):
    if root is None:
        return -1
    return 1 + max(find_height(root.left), find_height(root.right))
    

print(find_height(root))


#Size of the tree
def size_of_tree(root):
    if root is None:
        return 0
    return size_of_tree(root.left) + size_of_tree(root.right) +1

print(size_of_tree(root))