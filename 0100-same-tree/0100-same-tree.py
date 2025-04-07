# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def compareTrees(p, q):
            if not p and not q:
                return True 
            if (not p and q) or (p and not q) :
                return False 
            if p.val != q.val:
                return False
            leftSubTree = compareTrees(p.left,q.left)
            rightSubTree = compareTrees(p.right,q.right)
            return leftSubTree and rightSubTree #you need to use and instead of == to compare since False == False is True 
        return compareTrees(p,q)

