# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        post order 
        maxDepth(root.left)
        when we reach none, we return none and this when the max is calculated 
        if no return then we just a
        '''
        if not root:
            return 0
        
        height_lhs = 1+self.maxDepth(root.left)
        height_rhs = 1+ self.maxDepth(root.right)
        return max(height_lhs, height_rhs)
        

      
     
             

        


        