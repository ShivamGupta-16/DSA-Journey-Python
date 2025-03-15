class TreeNode:
    def __init__(self,value=0, left = None, right= None):
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


def findPreSuc(root, key):
    pre, suc = None, None
    if not root:
        return None, None
    
    while root:
        if root.val == key:
            if root.left:
                pre = root.left
                while pre.right:
                    pre = pre.right
            if root.right:
                suc = root.right
                while suc.left:
                    suc = suc.left

            return pre, suc



        elif root.val >key:
            #Move to left subtree
            suc = root
            root= root.left

        else:
            # Move to right subtree
            pre = root
            root = root.right

    return pre, suc

key = 55
p,q = findPreSuc(root,key)
print("Predecessor is : ", p.val if p else "None")
print("Successor is : ", q.val if q else "None")