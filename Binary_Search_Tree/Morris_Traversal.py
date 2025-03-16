# TreeNode class definition

class TreeNode:
    def __init__(self, value = 0, left= None, right = None):
        self.val = value
        self.left = left
        self.right = right

root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

def morris_traversal(root):
    current = root
    while current:
        if not current.left :
            print(current.val ,end =" ")
            current = current.right

        else:
            pre = current.left
            while pre.right and pre.right != current:
                    pre = pre.right

            if not pre.right:
                 pre.right = current
                 current = current.left
            else:
                 pre.right = None
                 print(current.val, end=" ")
                 current = current.right

morris_traversal(root)