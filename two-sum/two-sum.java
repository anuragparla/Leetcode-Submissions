import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer,Integer> ht = new Hashtable<>(); //no dynamic dispatch since Hashtable extends Dictionary.
        int diff = 0;//index=0;;
        int[] res = new int[2];
        for(int i=0;i<nums.length;i++){
            //diff = target-nums[i];
            if(ht.containsKey(target-nums[i])){
                res[index] =i; 
                index++;
                res[index] = ht.get(target-nums[i]);
                return res;  // placing a return statement here reduces running time by 3ms
            }
            else{
                ht.put(nums[i],i);  // lhs is value and the rhs is the index of the array.
            }
        }
        
        
    }
}
