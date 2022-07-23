import java.util.*;
class Solution {
    public boolean checkIfExist(int[] arr) {
        Hashtable<Integer,Integer> check = new Hashtable<>();
        for(int i = 0; i < arr.length; i++) {
            if((arr[i] % 2 == 0 && check.containsKey(arr[i] / 2)) || check.containsKey(arr[i] * 2 )) {
                return true;
            }
            else 
                check.put(arr[i],1);
        }
        return false;
    }
}