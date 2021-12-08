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
    public TreeNode searchBST(TreeNode root, int val) {
        TreeNode currentNode = root;
        while(currentNode != null) {
            if (val < currentNode.val) {
                currentNode = currentNode.left;
            }
            else if (val > currentNode.val) {
                currentNode = currentNode.right;
            }
            else {
                return currentNode;
            }
        }
        return null;
    }
}