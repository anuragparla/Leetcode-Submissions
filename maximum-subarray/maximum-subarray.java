class Solution {
    public int maxSubArray(int[] nums) {
        int maxSum = Integer.MIN_VALUE,sum=0;
        for(int i=0;i<nums.length;i++){
            sum = max(nums[i],sum+nums[i]);
            maxSum = max(maxSum,sum);
        }
        return maxSum;
    }
    private int max(int nums_i,int sum){
        if(nums_i>sum){
            return nums_i;
        }
        else{
            return sum;
        }
    }
}