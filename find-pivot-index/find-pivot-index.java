class Solution {
    public int pivotIndex(int[] nums) {
        int leftSum = 0;
        int totalSum = 0;
        for(int i:nums) {
            totalSum += i;
        }
        for(int j = 0; j<nums.length; j++) {
            if(leftSum == totalSum - leftSum - nums[j])
                return j;
            leftSum += nums[j];
        }
        return -1;
    
    }
}