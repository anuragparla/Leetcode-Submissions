# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        recursive approach
        '''
        if root is None:
            return None
        return self.lca(root, p, q)
    
    def lca(self, root, p, q):
        if root is None:
            return 
        
        elif root.val < p.val and root.val < q.val:
            return self.lca(root.right, p, q)
        
        elif root.val > p.val and root.val > q.val:
            return self.lca(root.left, p, q)
        
        else:
            return root
        
        