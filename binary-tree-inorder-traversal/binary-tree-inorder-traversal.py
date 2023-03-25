# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = []
        res = []
        stack.append(root)
        #print(stack[0].val)
        while stack:
            while root != None and root.left != None:
                print('entered the left subtree')
                stack.append(root.left)
                root = root.left
            temp = stack.pop()
            
            res.append(temp.val)
            print(res)
            if temp != None and temp.right != None:
                
                root = temp.right
                stack.append(root)
        return res