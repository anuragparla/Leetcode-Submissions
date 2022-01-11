class Solution {
    public void moveZeroes(int[] nums) {
        // using two pointer 2 pick and place the number
        int j = 0;
        for(int i = 0; i<nums.length;i++) {
            if(nums[i] != 0)
            {
                nums[j] = nums[i];
                j++;
            }
                
            
         }
        while(j < nums.length)
        {
            nums[j] = 0;
            j++;
        }
    }
}