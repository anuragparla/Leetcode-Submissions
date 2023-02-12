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
    List<Integer> res = new ArrayList<>();
    public List<Integer> postorderTraversal(TreeNode root) {
    // if(root == null)
    //     return res;
    //  postorderTraversal(root.left);
    //  postorderTraversal(root.right);
    //  res.add(root.val);
    //  return res;
        
    TreeNode curr = root;
        TreeNode temp = null;
        if(curr == null)
            return res;
    Stack<TreeNode> st = new Stack<>();
        while(!st.isEmpty() || curr != null) {
            if(curr != null){
                st.push(curr);
                curr = curr.left;
            }
            else {
                temp = st.peek().right;
                if(temp == null)
                {
                   temp = st.pop();
                   res.add(temp.val);
                
                while(!st.isEmpty() && temp == st.peek().right)
                {
                    temp = st.pop();
                    res.add(temp.val);
                }
                }
                  else {
                curr = temp;
                }  
                    
            }
            
        }
        return res;
    }
      
}