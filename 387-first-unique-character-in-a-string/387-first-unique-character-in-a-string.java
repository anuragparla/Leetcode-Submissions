class Solution {
    public int firstUniqChar(String s) {
        Map<Character,Integer>m = new HashMap<>();
        HashSet<Character> hs = new HashSet<>();
        int minIndex = s.length()-1;
        for(int i = 0; i<s.length();i++) {
            if(m.containsKey(s.charAt(i))  ) {
                m.remove(s.charAt(i));
                hs.add(s.charAt(i));
                
                
            }
            else {
                if(!hs.contains(s.charAt(i)))
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
    
        return minIndex;
        
    }
    
}