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

        call stack explained:
        1+maxdepth(3.left):
            root = 9
            1+maxdepth(9.left): # value is 1+0 = 1 
                root = None
                return 0 
            now when 0 is returned, the call maxdepth(9.left) is replaced with return value i.e 0 
            now that a return happend we will proceed to next line 
            1+maxdepth(9.right): # value is 1+0 = 1 
                root = None 
                return 0 

            return max(1,1) = 1 i.e maxdepth(3.left) = 1 => 1+ 1 = 2 
        since return happened, next line is executed 
        1+maxdepth(3.right): # 1 + 2 = 3 
            root = 20 
            1+maxdepth(20.left): # 1+1 = 2 
                root = 15
                1+maxdepth(15.left): 1+ 0 = 1 
                    root = None 
                    return 0
                1+maxdepth(15.right): 1+ 0 = 1 
                    root = None 
                    return 0 
                return max(1,1) = 1 
            1+maxdepth(20.right): # 2 
                root = 7 
                1+maxdepth(7.left): # 1
                    root = None
                    return 0
                1+maxdepth(7.right): # 1 
                    root = None
                    return 0
            return max(2,2)
        return max(2,3)
        exit 
        '''
        if not root:
            return 0
        
        height_lhs = 1+self.maxDepth(root.left)
        height_rhs = 1+ self.maxDepth(root.right)
        return max(height_lhs, height_rhs)
        

      
     
             

        


        