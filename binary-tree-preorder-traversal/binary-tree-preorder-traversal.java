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
     List<Integer>result = new ArrayList();
    public List<Integer> preorderTraversal(TreeNode root) {
      //NLR 
        /*
        Stack<TreeNode> stck = new Stack();
        List<Integer>result = new ArrayList();
        
        TreeNode curr = root;
        if (curr == null){
            return result;
        }
        while(curr != null || !stck.isEmpty()) {
            while(curr != null) {
                stck.push(curr);
                result.add(curr.val);
                curr = curr.left;
            }
            curr = stck.pop();
            curr = curr.right;
        }
        return result; */
        if(root == null)return result;
        result.add(root.val);
        preorderTraversal(root.left);
        preorderTraversal(root.right);
        return result;
    }
}