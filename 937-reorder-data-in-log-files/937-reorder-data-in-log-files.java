import java.util.*;
class Solution {
    public String[] reorderLogFiles(String[] logs) {
        Comparator<String> cmp = new Comparator<String>(){
        @Override
        public int compare(String logs1, String logs2) {
            String[] split1 = logs1.split(" ",2);
            String[] split2 = logs2.split(" ",2);
            
            boolean isDigit1 = Character.isDigit(split1[1].charAt(0));
            boolean isDigit2 = Character.isDigit(split2[1].charAt(0));
            
            if(!isDigit1 && !isDigit2) {
                if(split1[1].compareTo(split2[1]) != 0)
                    return split1[1].compareTo(split2[1]);
                else 
                    return split1[0].compareTo(split2[0]);
            }
            else if(!isDigit1 && isDigit2) 
                return -1 ;
            else if (isDigit1 && !isDigit2)
                return 1;
            else 
                return 0;
            
         
        }
        };
        
        Arrays.sort(logs,cmp);
        return logs;
    }
}