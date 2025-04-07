# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ''' 
        Use post order traversal and dfs 
        at every sub tree calculate height diff. if it's >1 then false
        Space complexity: O(H) where H is the height of the tree which is 
        best case O(logN) and worst O(N)
        Time complexity: O(N) where N is the number of nodes 
        '''
        balanced = [True]
        def computeHeight(root):
            if not root:
                return 0
            leftSubTreeHeight = computeHeight(root.left)
            rightSubTreeHeight = computeHeight(root.right)
            difference = abs(leftSubTreeHeight - rightSubTreeHeight)
            if difference >1:
                balanced[0] = False
            return 1 + max(leftSubTreeHeight,rightSubTreeHeight)
        if root:
            computeHeight(root)
        return balanced[0]

        
        
                
