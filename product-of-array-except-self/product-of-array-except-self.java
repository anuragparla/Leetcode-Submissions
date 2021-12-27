class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix_sum = new int[nums.length];
        int[] postfix_sum = new int[nums.length];
        int[] res = new int[nums.length];
        int prod = 1;
        
        for(int i = 0; i<nums.length;i++) {
            prod = prod*nums[i];
            prefix_sum[i] = prod;
        }
        
        prod = 1;
        
        for(int i = nums.length-1;i>=0;i--) {
            prod = prod * nums[i];
            postfix_sum[i] = prod;
        }
        
        for(int i =0;i<nums.length;i++) {
            if (i>0 && i<nums.length-1) {
                res[i] = prefix_sum[i-1]*postfix_sum[i+1];
            }
            else if (i == 0) {
                res[i] = postfix_sum[i+1];
            }
            else {
                res[i] = prefix_sum[i-1];
            }
        }
        
        return res;
    }
}