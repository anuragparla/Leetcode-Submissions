class Solution {
    //private boolean isDuplicate()
    public int lengthOfLongestSubstring(String s) {
        char[] str = s.toCharArray();
        int lp = 0;
        int rp = 0;
        int max = 0;
        
        HashSet<Character> hs = new HashSet();
        while(lp <str.length && rp <str.length) {
            if(hs.contains(str[rp])) {
                while(lp<=rp) {
                    
                    hs.remove(str[lp]);
                    lp +=1;
                    if(!hs.contains(str[rp]))
                        break;
                }
            }
            else {
                hs.add(str[rp]);
                rp +=1;
            }
            max = Math.max(max,(rp-lp));
        }
        return max;
    }
}