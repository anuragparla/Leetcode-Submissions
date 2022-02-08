import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> numsMap = new HashMap();
        int[] res = new int[2];
        for ( int i = 0 ;i<nums.length;i++) {
            if(numsMap.containsKey(target-nums[i])){
                res[0] = i;
                res[1] = numsMap.get(target-nums[i]);
                return res;
            }
            else {
                numsMap.put(nums[i],i);
            }
            
        }
        return res;
    }
}