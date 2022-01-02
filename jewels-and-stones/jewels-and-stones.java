class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        char[] j = jewels.toCharArray();
        Map<Character,Integer> jewelTable = new HashMap();
        int jewelCount = 0;
        for(int i = 0; i<j.length;i++) {
            jewelTable.put(j[i],i);
        }
        
        char[] s = stones.toCharArray();
        for(int k = 0; k<s.length;k++) {
            if(jewelTable.containsKey(s[k])) {
                jewelCount +=1;
            }
        }
        return jewelCount;
    }
}