class Solution {
    public boolean checkIfExist(int[] arr) {
        /*
        for(int i=0;i<arr.length-1;i++){
            for(int j=i+1;j<arr.length;j++){
                if(arr[i]==2*arr[j] || arr[j]==2*arr[i]){
                    return true;
                }
            }
            
        }
        return false;
        */
         HashSet hs = new HashSet();
        for(int i=0;i<arr.length;i++){
            if(hs.contains(arr[i]*2) || (arr[i]%2==0 && hs.contains(arr[i]/2))){
                return true;
            }
            hs.add(arr[i]);
        }
        return false;
    }
}
