# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.stackk = []
        self.res = []
        while len(self.stackk) != 0 or root:
            while root:
                self.res.append(root.val)
                self.stackk.append(root)
                root = root.left
            root = self.stackk.pop()
            root = root.right
        return self.res
