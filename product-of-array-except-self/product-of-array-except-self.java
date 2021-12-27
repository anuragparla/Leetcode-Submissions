class Solution {
    public int[] productExceptSelf(int[] nums) {
        /* O(N)T O(N)S 
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
        }*/
        
        /**
        O(N)T O(1)S
        */
        int[] res = new int[nums.length];
        // calculating the prefix till last but one element and storing it in the output array
        int prefix = 1;
        res[0] = prefix;
        for(int i = 0; i<nums.length-1;i++) {
            prefix = prefix*nums[i];
            res[i+1] = prefix;
        }
        // calculating the postfix from nums[length-2] element and directly multiplying with the content of the output array which is the prefixes 
        int postfix = nums[nums.length-1];
        for(int j=nums.length-2;j>=0;j--) {
            res[j]=res[j]*postfix;
            postfix = postfix*nums[j]; 
        }
        return res;
    }
}
