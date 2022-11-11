class Solution {
    public int removeDuplicates(int[] nums) {
        int firstPointer = 0;
         int secondPointer = 0;
        if(nums.length < 2) return 1;
        for(secondPointer = 1; secondPointer < nums.length; secondPointer ++)
        {
            if(nums[firstPointer] != nums[secondPointer])
            {
                nums[firstPointer +1] = nums[secondPointer]; 
                firstPointer += 1;
            }
        }
        return firstPointer +=1;
    }
}