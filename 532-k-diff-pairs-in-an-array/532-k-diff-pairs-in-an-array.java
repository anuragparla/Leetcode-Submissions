class Solution {
    public int findPairs(int[] nums, int k) {
        Map<Integer,Integer> pairs = new HashMap();
        int diff = 0;
        int count = 0;
        for(int i = 0 ; i<nums.length;i++) {
            if(pairs.containsKey(nums[i])) {
                pairs.put(nums[i],pairs.get(nums[i])+1);
            }
            else {
                pairs.put(nums[i],1);
            }
            
        }
        for(Map.Entry<Integer, Integer> entry : pairs.entrySet()){
            if(k==0){
                if(entry.getValue()>=2)
                    count++;
            }
            else{
                if(pairs.containsKey(entry.getKey()+k))
                    count++;
            }
        
        }
             
    
        return count;
}
}