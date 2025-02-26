# Defined Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function for Left boundary
def printLeftBoundary(root, boundary):
    if root is None:
        return
    if root.left:
        boundary.append(root.data)
        printLeftBoundary(root.left, boundary)
    elif root.right:
        boundary.append(root.data)
        printLeftBoundary(root.right, boundary)

# Function for Right boundary
def printRightBoundary(root, boundary):
    if root is None:
        return
    if root.right:
        printRightBoundary(root.right, boundary)
        boundary.append(root.data)
    elif root.left:
        printRightBoundary(root.left, boundary)
        boundary.append(root.data)

# Function for Leaves
def printLeaves(root, boundary):
    if root is None:
        return
    printLeaves(root.left, boundary)
    if root.left is None and root.right is None:
        boundary.append(root.data)
    printLeaves(root.right, boundary)

# Combined Function for Boundary of binary tree
def printBoundary(root):
    boundary = []
    if root is None:
        return boundary
    boundary.append(root.data)
    printLeftBoundary(root.left, boundary)
    printLeaves(root.left, boundary)
    printLeaves(root.right, boundary)
    printRightBoundary(root.right, boundary)
    return boundary

# Example usage:
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
root.right.left = Node(6)
root.right.left.left = Node(7)
root.right.left.left.left = Node(9)
root.right.left.right = Node(8)
root.right.left.right.right = Node(10)

boundaryTraversal = printBoundary(root)
print("Boundary Traversal:", boundaryTraversal)