class Solution {
    public int removeDuplicates(int[] nums) {
        int i = 0; 
        int j = i+1;
        boolean foundDup = false;
        while(j < nums.length) {
            if(nums[i] != nums[j] && foundDup == false){
                j +=1;
                i +=1;
            }
            else if(nums[i] != nums[j] && foundDup == true)
            {
                i += 1;
                nums[i] = nums[j];
                j += 1;
            }
            else {
                j +=1;
                foundDup = true;
            }
        }
        return i+1;
    }
}