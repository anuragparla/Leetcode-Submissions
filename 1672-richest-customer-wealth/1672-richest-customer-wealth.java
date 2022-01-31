class Solution {
    public int maximumWealth(int[][] accounts) {
        int row_length = accounts.length;
        int coloumn_length = accounts[0].length;
        int max = 0;
        int sum = 0;
        for(int i = 0 ;i<row_length;i++) {
            for(int j = 0;j<coloumn_length;j++) {
                sum = sum+accounts[i][j];
            }
            if(sum>max){
                max = sum;
            }
            sum = 0;
        }
        return max;
    }
}