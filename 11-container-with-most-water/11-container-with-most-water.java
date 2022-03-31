class Solution {
    public int maxArea(int[] height) {
        if(height.length <1)
            return 0;
        int lp = 0; 
        int rp = height.length-1;
        int maxArea = 0;
        int tempArea = 0;
        int tempHeight = 0;
        while(lp<rp) {
            if(height[lp]<height[rp])
            {
                tempHeight = height[lp];
                tempArea = tempHeight * (rp-lp);
                maxArea = Math.max(maxArea,tempArea);
                lp++;
            }
            else {
                tempHeight = height[rp];
                 tempArea = tempHeight * (rp-lp);
                maxArea = Math.max(maxArea,tempArea);
                rp --;
            }
                
            
        }
       return maxArea; 
    }
}