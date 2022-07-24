class Solution {
    public int[] replaceElements(int[] arr) {
        int temp = 0;
        int max = Integer.MIN_VALUE;
        for(int i = arr.length - 1; i>=0; i--) {
            if ( i == arr.length - 1) {
                temp = arr[i];
                if(max < temp)
                    max = temp;
                arr[i] = -1;
            }
            else {
                temp = arr[i];
                arr[i] = max;
                if(max < temp)
                    max = temp;
            }
        }
        return arr;
    }
}