class Solution {
    private int[] intersection(HashSet<Integer>set1, HashSet<Integer>set2){
        int[] res = new int[set1.size()];
        int index = 0;
        for(Integer r:set1){
            if(set2.contains(r))
                res[index++] = r;
        }
        return Arrays.copyOf(res, index);
        
    }
    
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> numSet1 = new HashSet();
        HashSet<Integer> numSet2 = new HashSet();
        
        for(Integer i: nums1){
            numSet1.add(i);
        }
        for(Integer j: nums2){
            numSet2.add(j);
        }
        
        if(numSet1.size()<numSet2.size())
            return intersection(numSet1,numSet2);
        else 
            return intersection(numSet2, numSet1);
    }
}