class Solution {
    
    private int binSearch(int[] nums, int target, Boolean leftBiase){
        int lp = 0;
        int rp = nums.length-1;
        int mid = 0;
        int index = -1;
        while(lp<=rp){
            mid = (lp+rp)/2;
            if(nums[mid] == target ){
                System.out.println("target matched");
                index=mid;
                if(leftBiase) {
                    rp = mid-1;
                }
                else {
                    lp = mid+1;
                }
            }
            else if(nums[mid]<target) {
                lp = mid+1;
            }
            else if(nums[mid]>target) {
                rp = mid-1;
            }
        }
        return index;
    }
    public int[] searchRange(int[] nums, int target) {
        int[] result = new int[2];
        result[0] = -1;
        result[1] = -1;
        int leftindex = binSearch(nums,target,true);
        int rightindex = binSearch(nums,target,false);
        if ((leftindex | rightindex) == -1) {
            return result;
        }
        else {
            result[0] = leftindex;
            result[1] = rightindex;
            return result;
        }
    }
}