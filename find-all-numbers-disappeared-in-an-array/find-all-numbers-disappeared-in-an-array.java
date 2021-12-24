import java.util.*;
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        Hashtable<Integer,Integer> ht = new Hashtable();
        List<Integer> l = new ArrayList();
        for (int i = 0; i<nums.length;i++) {
            ht.put(nums[i],i);
        }
        
        for(int j = 1; j<nums.length+1; j++) {
            if (ht.containsKey(j)) {
                continue;
            }
            else {
                l.add(j);
            }
        }
        return l;
    }
}