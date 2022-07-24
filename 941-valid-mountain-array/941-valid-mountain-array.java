class Solution {
    public boolean validMountainArray(int[] arr) {
        int i = 0;
        int j = i+1;
        boolean isClimbingUp = false;
        boolean isClimbingDown = false;
        while(j<arr.length) {
            if(arr[i]< arr[j]) {
                i +=1;
                j +=1;
                isClimbingUp = true;
            }
            else {
                isClimbingDown = true;
                break;
                //return false;
            }
        }
        while(j<arr.length) {
            if(arr[i] > arr[j]) {
                j += 1;
                i += 1;
            }
            else {
                return false;
            }
        }
        return isClimbingDown && isClimbingUp; 
    }
}