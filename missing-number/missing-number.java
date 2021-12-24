import java.util.*;
class Solution {
    public int missingNumber(int[] nums) {
        Hashtable <Integer,Integer> ht = new Hashtable<Integer,Integer>();
        for ( int i = 0; i<nums.length;i++) {
            ht.put(nums[i],i);
        }
        for(int i=0;i<nums.length+1;i++) {
            if(ht.containsKey(i)) {
                continue;
            }
            else {
                return i;
            }
        }
        return 0;
    }
}