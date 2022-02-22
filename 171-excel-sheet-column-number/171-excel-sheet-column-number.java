class Solution {
    public int titleToNumber(String columnTitle) {
         Map<Character,Integer> charStorage = new HashMap();
        storeChars(charStorage);
        int length = columnTitle.length();
        int sum = 0;
        int temp = length -1;
        for ( int j = 0; j<length; j++) {
            sum = sum + (int )Math.pow(26,temp) *           charStorage.get(columnTitle.charAt(j));
            temp -= 1; 
            
        }
        return sum;  
               
    }
    /**
    This function will store the characters and it's value
    */
    
    private static void storeChars(Map charStorage) {
           int value = 1;
           for (int i = 65; i<91; i++) {
            charStorage.put((char)i, value);
            value += 1;
        } 
        }
    }
