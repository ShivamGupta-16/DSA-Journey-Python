class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def LOT_Right_to_Left(root):
    if root is None:
        return
    
    queue= [root]

    while queue:
        node = queue.pop(0)
        print(node.data, end=' ')

        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


print("Level order traversal from Right to Left: ")
LOT_Right_to_Left(root)