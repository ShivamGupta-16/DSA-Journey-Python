#Creating BST

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right= None

class BST:
    def __init__(self):
        self.root = None

    #Insert elements
    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return 
        current = self.root

        while True:
            if current.value > value:
                if current.left is None:
                    current.left = new_node
                    return 
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def preorderTraversal(self, node):
        if node is None:
            return
        print(node.value, end=" ")   
        self.preorderTraversal(node.left )
        self.preorderTraversal(node.right )

    def inOrderTraversal(self, node):
        if node is None:
            return
        self.inOrderTraversal(node.left)
        print(node.value, end = " ")
        self.inOrderTraversal(node.right)

    def postOrderTraversal(self, node):
        if node is None:
            return

        self.postOrderTraversal(node.left)
        self.postOrderTraversal(node.right)
        print(node.value, end= " ")


data = [6,2,8,4,9,11,3,1,0]
bst = BST()
for item in data:
    bst.insert(item)

print("\n Preorder of BST: ")
bst.preorderTraversal(bst.root)

print("\n Inorder of BST: ")
bst.inOrderTraversal(bst.root)

print("\n postorder of BSt: ")
bst.postOrderTraversal(bst.root)