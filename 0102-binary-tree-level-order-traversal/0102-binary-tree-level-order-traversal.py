# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        self.res = []
        self.queue = deque()
        
        self.queue.append(root)
        while self.queue:
            size = len(self.queue)
            level = list()
            for i in range(size):
                node = self.queue.popleft()
                level.append(node.val)
                if node.left:
                    self.queue.append(node.left)
                if node.right:
                    self.queue.append(node.right)
            self.res.append(level)
        return self.res


        
        