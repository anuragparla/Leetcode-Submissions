# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None or len(preorder) == 0 or inorder is None or len(inorder) == 0:
            return None
        
        root = TreeNode(preorder[0])
        rootIdx = -1 
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                rootIdx = i
        inorderLeft = inorder[0:rootIdx]
        inoderRight = inorder[rootIdx + 1:]
        preorderLeft = preorder[1:rootIdx + 1]
        preorderRight = preorder[rootIdx + 1:]
        root.left = self.buildTree(preorderLeft, inorderLeft)
        root.right = self.buildTree(preorderRight,inoderRight )
        return root

        