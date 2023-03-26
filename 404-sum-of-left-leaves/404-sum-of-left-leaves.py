# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque 
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = deque([(root, False)])
        sum = 0
        while stack:
            curr, isLeft = stack.pop()
            if curr.left == None and curr.right == None and isLeft:
                sum += curr.val 
            if curr.left:
                stack.append((curr.left, True))
            if curr.right:
                stack.append((curr.right, False))
           
        return sum

