import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Hashtable<Integer,Integer> ht = new Hashtable<>();
        int diff = 0,index=0;;
        int[] res = new int[2];
        for(int i=0;i<nums.length;i++){
            diff = target-nums[i];
            if(ht.containsKey(diff)){
                res[index] =i; 
                index++;
                res[index] = ht.get(diff);
            }
            else{
                ht.put(nums[i],i);
            }
        }
        return res;
        
    }
}