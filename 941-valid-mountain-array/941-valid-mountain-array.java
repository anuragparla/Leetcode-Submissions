class Solution {
    public boolean validMountainArray(int[] arr) {
        
        int i=0;
        
        while(i<arr.length-1 && arr[i]<arr[i+1]){
            i+=1;
        }
        
        if(i==0 || i==arr.length-1){
            return false;
        }
        
        while(i<arr.length-1 && arr[i]>arr[i+1]){
            i+=1;
        }
        
        return i == arr.length-1;
    }
}


    