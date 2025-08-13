# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        self.res = []
        self.recurse(root)
        return self.res
    
    def recurse(self, root):
        if root is None:
            return
        self.recurse(root.left)
        self.res.append(root.val)
        self.recurse(root.right)

        