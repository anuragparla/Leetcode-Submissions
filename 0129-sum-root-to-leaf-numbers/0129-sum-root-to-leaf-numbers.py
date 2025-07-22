# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    totalSum = 0 
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.dfs(root, 0)
        return self.totalSum

    def dfs(self, root, currentSum = 0):
        if root is None:
            return
        currentSum = currentSum * 10 + root.val
        self.dfs(root.left, currentSum)
        if root.left is None and root.right is None:
            self.totalSum = self.totalSum + currentSum
            return 
        self.dfs(root.right, currentSum)
    
    



        