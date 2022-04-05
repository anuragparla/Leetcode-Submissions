class Solution {
    public int maxArea(int[] height) {
        /* O(n^2) doesn't work for this
        int maxArea = Integer.MIN_VALUE;
        for(int i = 0; i<height.length; i++) {
            for(int j = i+1; j<height.length; j++) {
                if(height[i]<height[j])
                    maxArea = Math.max((height[i]*(j-i)),maxArea);
                else {
                     maxArea = Math.max((height[j]*(j-i)),maxArea);
                }
            }
        }*/
        // 2 pointer approach
        int maxArea = Integer.MIN_VALUE;
        int lp = 0;
        int rp = height.length -1 ;
        while(lp < rp) {
            if(height[lp]<height[rp])
            {
                maxArea = Math.max((height[lp]*(rp-lp)),maxArea);
                lp +=1;
            }
            else {
                maxArea = Math.max((height[rp]*(rp-lp)),maxArea);
                rp -=1;
            }
                 
        }
        return maxArea;
    }
}