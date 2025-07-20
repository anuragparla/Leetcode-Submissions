# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mapp = {}
    idx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if preorder is None or len(preorder) == 0 or inorder is None or len(inorder) == 0:
            return None
        
        for i in range(len(inorder)):
            self.mapp[inorder[i]] = i 
        
        return self.createTree(preorder, 0, len(inorder)-1)
    
    def createTree(self, preorder, start, end):
        if start > end:
            return None 
        rootVal = preorder[self.idx]
        self.idx += 1
        root = TreeNode(rootVal)
        rootIdx = self.mapp[rootVal]
        root.left = self.createTree(preorder, start, rootIdx - 1)
        root.right = self.createTree(preorder, rootIdx + 1, end)
        return root  
        '''
        Recursive method causes the time complexity to be O(N^2)
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
        '''

        