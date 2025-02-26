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

#           1
#        2     3
#    4      5


def preorder_iterative(root):
    stack =[]
    result =[]
    if not root:
        return result
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


print(preorder_iterative(root))