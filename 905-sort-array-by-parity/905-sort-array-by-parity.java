class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int i = 0; 
        int j = nums.length - 1;
        int temp;
        while ( i<j) {
            if(nums[i] % 2 == 0 && nums[j] %2 != 0){
                i ++;
                j --;
            }
            else if (nums[i] % 2 == 0 && nums[j] % 2 == 0) {
                i ++;
            }
            else if (nums[i] % 2 != 0 && nums[j] % 2 == 0) {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                i ++;
                j --;
            }
            else {
                j --;
            }
        }
        return nums;
    }
}