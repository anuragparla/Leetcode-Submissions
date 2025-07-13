# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isValid = False 
    prev = None 
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True 
        self.isValid = True
        self.inorder(root)
        return self.isValid

    
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        if self.prev is not None and self.prev.val >= root.val:
            self.isValid = False
        self.prev = root
        self.inorder(root.right)





        

        