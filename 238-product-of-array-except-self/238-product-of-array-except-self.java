class Solution {
    public int[] productExceptSelf(int[] nums) {
        /*
        Map<Character,Integer>m = new HashMap<>();
        HashSet<Character> hs = new HashSet<>();
        int minIndex = s.length()-1;
        for(int i = 0; i<s.length();i++) {
            if(m.containsKey(s.charAt(i))) {
                m.remove(s.charAt(i));
                if(!hs.contains(s.charAt(i))) {
                    hs.add(s.charAt(i));
                }
                
            }
            else {
                m.put(s.charAt(i),i);
            }
        }
        for(int val: m.values()) {
            if(val < minIndex)
                minIndex = val;
        }
        //if(minIndex >=0)
        if(m.isEmpty()) {
            return -1;
        } 
    
        return minIndex; */
        int[] res = new int[nums.length];
        res[0] = 1;
        // calculating the prefix products
        for(int i = 1; i<nums.length;i++) {
            res[i] = res[i-1] *nums[i-1];
        }
        
        // calculating the postfix product and also calculating the final product without using additional memory
        int r = 1;
        for(int j = nums.length - 1; j>=0; j--) {
            res[j] = res[j] * r;
            r = r *nums[j];
        }
        return res;
    }
    
}