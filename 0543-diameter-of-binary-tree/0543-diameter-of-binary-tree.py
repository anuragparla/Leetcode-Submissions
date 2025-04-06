# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        '''
        diameter of a binary tree is the sum of height of left sub tree and height
        of a right sub tree
        height of a sub tree = 1 + max(left_sub_height, right_sub_height)
        '''
        # passing a primitive type to a func results in pass by val
        # to avoid that we are passing it as list, so that each call stack will still reference
        # the same variable "largest_diameter"
        largest_diameter = [0] 
        

        def computeHeight (root):
            if not root:
                return 0 
            left_subtree_height = computeHeight(root.left)
            right_subtree_height = computeHeight(root.right)
            current_diameter = left_subtree_height + right_subtree_height
            largest_diameter[0] = max(largest_diameter[0], current_diameter)

            return 1 + max(left_subtree_height, right_subtree_height)
        
        computeHeight(root)
        return largest_diameter[0]



        