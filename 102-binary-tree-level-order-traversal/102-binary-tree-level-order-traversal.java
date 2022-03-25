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
    
    //List<List<Integer>> res = new ArrayList();
    /*private void helper(TreeNode root, int level) { 
        
        if(res.size() == level)
            res.add(new ArrayList());
        res.get(level).add(root.val);
        if(root.left != null)
            helper(root.left,level+1);
        if(root.right != null)
            helper(root.right, level+1);
    }
    */
    public List<List<Integer>> levelOrder(TreeNode root) {
        /*
        int level = 0;
        
        if(root == null)
            return res;
        helper(root,level);
        return res; 
        */
    
    // iterative approach 
    int level = 0; 
    List<List<Integer>> res = new ArrayList();
    Queue<TreeNode> q = new LinkedList();
    if(root == null)
        return res;
    q.add(root);
    
    while(! q.isEmpty()) {
        res.add(new ArrayList());
        int tempQSize = q.size();
        for(int i = 0 ; i<tempQSize; i++) {
            TreeNode temp = q.remove();
            res.get(level).add(temp.val);
            if(temp.left != null)
                q.add(temp.left);
            if(temp.right != null)
                q.add(temp.right);
           
        }
         level++;
    }
        return res;
    }
}