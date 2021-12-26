import java.util.*;
class Solution {
    
    
    public int titleToNumber(String columnTitle) {
        /*
        ZY --> length is 2 ==> 26 * 26 + 25   
        AA --> 26 * value of first + the value of the last 
        AAA --> 26 * 26 * value of first + 26 * value of the second + value of the
        last
        AAAA --> length -1 * 26 * val of 
        AAAAAAA --> 26 ^ 6 * val of A + 26 ^ 5 * val of A so on STUVW
        F = 6 X 24 S 20 H 8 R 19 X 24 W 
        FXSHRXW --> 
        6 + 5+ 4 + 3 + 2 + 1  */        
        
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