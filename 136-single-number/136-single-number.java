class Solution {
    public int singleNumber(int[] nums) {
         HashMap<Integer, Integer> count = new HashMap();
        //Mapping of each unique element with number of repeatition
        for(int i = 0; i < nums.length; i++){
            if(count.containsKey(nums[i])){
                count.put(nums[i], count.get(nums[i])+1);
            }
            else{
                count.put(nums[i], 1);
            }
        }
        //iterate through the keySet and find which key has value of 1
        for(Integer key: count.keySet()){
            if(count.get(key) == 1){
                return key;
            }
        }
        return -1;
    }
}