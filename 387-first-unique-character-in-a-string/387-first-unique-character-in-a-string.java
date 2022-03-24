class Solution {
    public int firstUniqChar(String s) {
        // approach 1
        /*
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
    
        return minIndex; */
        
        // approach 2 iterating over the hashmap and storing fetching the count
        
        Map<Character,Integer> hm = new HashMap<>();
        for(int i = 0; i<s.length(); i++) {
            if(hm.containsKey(s.charAt(i)))
                hm.put(s.charAt(i),hm.get(s.charAt(i)) +1);
            else
                hm.put(s.charAt(i),1);
        }
        
        for(int j = 0; j<s.length();j++) {
            if(hm.get(s.charAt(j)) == 1)
                return j;
        }
        return -1;
    }
    
}