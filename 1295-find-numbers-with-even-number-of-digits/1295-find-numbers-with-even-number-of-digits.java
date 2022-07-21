class Solution {
    private boolean findNumberEvenOrOdd(int n) {
        int count = 0; 
        
        while(n != 0) {
            count += 1;
            n = n / 10;
        }
        if(count % 2 == 0)
            return true;
        else 
            return false;
    }
    public int findNumbers(int[] nums) {
        int finalCount = 0;
        for(int i :nums) {
            if(findNumberEvenOrOdd(i))
                finalCount += 1;
        }
        return finalCount;
    }
}