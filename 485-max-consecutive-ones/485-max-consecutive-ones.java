class Solution {
    public int findMaxConsecutiveOnes(int[] nums) { 
        int max = 0;
        int temp = 0;
        int res = 1;
        for(int i = 0; i<nums.length; i++) {
            if(nums[i] == 1){
                temp += 1;
            }
            else {
                temp = 0; 
            }
            if(temp>max)
                max = temp;
        }
           return max; 
    }
}