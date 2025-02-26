from collections import deque

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




def print_nth_level(root, n):
    if root is None:
        return 
    level = 0
    queue = deque([root])

    while queue:
        level_size = len(queue)
        if level ==n:
            for i in range(level_size):
                node = queue.popleft()
                print(node.val, end = " ")
            return 
        
        for _ in range(level_size):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        level+=1
    print("Level Not found")


print_nth_level(root,0)

