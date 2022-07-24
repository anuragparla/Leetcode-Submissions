class Solution {
    public void moveZeroes(int[] nums) {
        int nonZeroFoundAt = 0;
        for(int i = 0; i < nums.length; i++) {
            if(nums[i] != 0) {
                nums[nonZeroFoundAt] = nums[i];
                nonZeroFoundAt += 1;
            }
        }
        for(int j = nonZeroFoundAt; j< nums.length; j++) {
            nums [j] = 0;
        }
    }
}