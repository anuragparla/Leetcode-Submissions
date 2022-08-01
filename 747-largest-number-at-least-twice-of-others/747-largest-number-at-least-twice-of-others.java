class Solution {
    public int dominantIndex(int[] nums) {
        int max = 0;
        int index = 0;
        for(int i = 0; i<nums.length; i++) {
            if(max < nums[i])
            {
                 max = nums[i];
                index = i;
            }
               
        }
        for(int j = 0; j<nums.length; j++) {
            if(nums[j] != max){
                if(max >= 2 * nums[j]){
                    continue;
                }
                else {
                    return -1;
                }
            }
        }
        return index;
    }
}