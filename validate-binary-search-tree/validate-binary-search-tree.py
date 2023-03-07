# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def bst(self,root, low, high):
        if root == None:
            return True 
        if root.val <= low or root.val >= high:
            return False 
        return (self.bst(root.left, low, root.val) and self.bst(root.right,root.val, high))
    def isValidBST(self, root):   #  2 1 3 
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.bst(root,float("-inf"), float("inf"))
        