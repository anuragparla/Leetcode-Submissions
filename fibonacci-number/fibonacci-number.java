class Solution {
    public int fib(int n) {
        /*
        if(n <= 1) {
            return n;
        }
        else {
            return fib(n-2)+fib(n-1);
        }*/
    int[] fibArr = new int[n+1];
        if (n > 0) {
            fibArr[1] = 1;
        }
        if (n > 1) {
            for (int i = 2; i < n+1; i++) {
                fibArr[i] = fibArr[i-1] + fibArr[i-2];
            }
        }
    return fibArr[n];
}
    }
