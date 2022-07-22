class Solution {
    public int removeElement(int[] nums, int val) {
        int i = 0;
        int j = nums.length - 1;
        while ( i<=j) {
            if(nums[i] != val)
                i += 1;
            else if(nums[i] == val && nums[j] == val)
                j -= 1;
            else {
                nums[i] = nums[j];
                j -= 1;
                i += 1;
            }
        }
        return j+1;
    }
}