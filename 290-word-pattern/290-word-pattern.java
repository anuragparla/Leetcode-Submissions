class Solution {
    public boolean wordPattern(String pattern, String s) {
        
        
        
        String[] sArray = s.split(" ");
        //System.out.println()
        if(pattern.length() != sArray.length) {
            return false;
        }
        else {
            Map<Character,String>patternTable = new HashMap();
            for(int i = 0; i<pattern.length();i++) {
                if(patternTable.containsKey(pattern.charAt(i))) {
                    if(patternTable.get(pattern.charAt(i)).equals(sArray[i])) {
                        continue;
                    }
                    else {
                        return false;
                    }
                }
                else {
                    if(patternTable.containsValue(sArray[i])) {
                        return false;
                    }
                    else {
                        patternTable.put(pattern.charAt(i),sArray[i]);
                    }
                }
             }
            return true;
         }
        
        
     }
}