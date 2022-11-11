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
    /*
    // recursive approach
    TreeNode temp = null;
    public TreeNode invertTree(TreeNode root) {
        if(root == null) return root;
        temp = root.left;
        root.left = root.right;
        root.right = temp;
        invertTree(root.left);
        invertTree(root.right);
        return root; 
        */ 
    // iterative approach
    Stack<TreeNode> stash = new Stack<>();
    List<TreeNode> result = new ArrayList<>();
    TreeNode temp = null;
    public TreeNode invertTree(TreeNode root) {
        while(root != null || !stash.isEmpty()) {
            while(root != null) {
                temp = root.left;
                root.left = root.right;
                root.right = temp;
                stash.push(root);
                result.add(root);
                root = root.left;
            }
            root = stash.pop().right;
        }
        return result.isEmpty() ? null : result.get(0);
    }
}