/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int maxDepth(TreeNode root) {
        if (root == null)
            return 0;
        int depth = 0;
        
        return helper(root, depth);
    }
    
    private int helper(TreeNode root, int depth) {
        if(root == null){
            return depth;
        }
        int leftDepth = helper(root.left, depth+1);
        int rightDepth = helper(root.right, depth+1);
        return Math.max(leftDepth, rightDepth);
    }
    
}