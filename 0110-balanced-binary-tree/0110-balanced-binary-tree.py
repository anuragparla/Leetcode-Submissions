# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = self.checkHeight(root)

        if res == -1:
            return False
        else:
            return True
    
    def checkHeight(self,root):
        if root is None:
            return 0
        
        height_left = self.checkHeight(root.left)
        height_right = self.checkHeight(root.right)

        if height_left == -1 or height_right == -1:
            return -1
        
        if abs(height_left - height_right) <= 1:
            return 1+ max(height_left, height_right)
        else:
            return -1

        