class Solution {
    public int climbStairs(int n) {
       int[] stairPossibilities = new int[n+1];
       
        if(n == 1) {
            return 1;
        }
        
        stairPossibilities[1] = 1;
        stairPossibilities[2] = 2;
        
        for(int i=3;i<n+1;i++) {
            stairPossibilities[i] = stairPossibilities[i-1]+stairPossibilities[i-2];
        }
        return stairPossibilities[n];
    }
}