class Solution {
    public int findPeakElement(int[] nums) {
      //question asked in facebook, google and bloomberg 
       // using binary search to solve the problem 
        int l = 0;
        int r = nums.length-1;
        int mid = 0;
        while (l<r) { // here l<r and not l<=r. this is being done to prevent infinite looping  
            mid = l +(r-l)/2;
            if(nums[mid]<nums[mid+1]){
                l +=1;
            }
            else {
                r = mid;
            }
            
        }
        return l;
    }
}