class Solution {
    public int lengthOfLongestSubstring(String s) {
        /*
        // clementisacap
        int length = s.length();
        int startIndex = 0;
        String maxsub = "";
        String currsub = ""; 
        Map<Character,Integer> table = new HashMap();
        for ( int i=0; i<length;i++) {
            
            if (table.containsKey(s.charAt(i))) {
                int newStartIndex = Math.max(startIndex,table.get(s.charAt(i))+1);
                int count = newStartIndex;
                currsub = "";
                while(count<i+1) {
                    currsub = currsub+ s.charAt(count);
                    count +=1 ;
                    //System.out.println(currsub);
                }
                
                if (currsub.length() > maxsub.length())
                    maxsub = currsub;
               
                startIndex = newStartIndex;
                }
            else {
                table.put(s.charAt(i),i);
                currsub = currsub + s.charAt(i);
                //currsub.append(s.charAt(i));
                if (currsub.length()>maxsub.length()) {
                    maxsub = currsub;
                }
                
            }
            }
        //System.out.println(maxsub);
           return maxsub.length(); 
           
           */
        
        Map<Character, Integer> table = new HashMap<>();
        int[] longest = {0, 0};
        int startIndex = 0;
        char c;
        
        for(int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            
            if(table.containsKey(c)) {
                startIndex = Math.max(startIndex, table.get(c) + 1);
            }
            
            if(longest[1] - longest[0] < i + 1 - startIndex) {
                longest[0] = startIndex;
                longest[1] = i + 1;
            }
            
            table.put(c, i);
        }
        
        return longest[1] - longest[0];
        
        }
    }
