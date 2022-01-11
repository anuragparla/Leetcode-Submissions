class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] res = new int[nums.length];
        int p1 = 0;
        int p2 = nums.length -1;
        int p3 = nums.length -1;
        //for ( int i = 0; i<nums.length; i++) {
        while(p1<=p2) {
               if(Math.abs(nums[p1])>Math.abs(nums[p2])) {
                   res[p3] = nums[p1]*nums[p1];
                   p3--;
                   p1++;
               }
            else {
                res[p3] = nums[p2]*nums[p2];
                p3--;
                p2--;
            }
            
        }
         return res;
    }
            
            
    
}