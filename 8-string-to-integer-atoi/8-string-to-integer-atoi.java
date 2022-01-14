class Solution {
    public int myAtoi(String input) {
        // -4193 with words
        //char c = '9';
        //return c-'0';
        /*
        char[] arr = s.trim().toCharArray(); // [ -4193 with words]
        int sign = 1;
        int result = 0;
        int mul = 1;
        List<Integer> l = new ArrayList();
        
        for(int i = 0; i<arr.length;i++) {
            if(i == 0 && arr[i] == '-'){
                sign = -1;
                //continue;
            }
            else if ( i == 0 && arr[i] == '+'){
                sign = 1;
                //continue;
            }
            else {                  // 1)- 42   2) 42 words. 3) 
                if(arr[i] - '0' > 9) {
                    break;
                }
                else {
                    l.add(arr[i]-'0');
                }
            }
            
        }
        for(int j = l.size()-1;j>=0;j--) { //42 
            result += l.get(j)*mul;
            mul *= 10;
        }
        if(result > Integer.MAX_VALUE)
            return Integer.MAX_VALUE;
        else if (result < Integer.MIN_VALUE)
            return Integer.MIN_VALUE;
        else
        return result*sign;
        */
         int sign = 1; 
        int result = 0; 
        int index = 0;
        int n = input.length();
        
        // Discard all spaces from the beginning of the input string.
        while (index < n && input.charAt(index) == ' ') { 
            index++; 
        }
        
        // sign = +1, if it's positive number, otherwise sign = -1. 
        if (index < n && input.charAt(index) == '+') {
            sign = 1;
            index++;
        } else if (index < n && input.charAt(index) == '-') {
            sign = -1;
            index++;
        }
        
        // Traverse next digits of input and stop if it is not a digit
        while (index < n && Character.isDigit(input.charAt(index))) {
            int digit = input.charAt(index) - '0';

            // Check overflow and underflow conditions. 
            if ((result > Integer.MAX_VALUE / 10) || 
                (result == Integer.MAX_VALUE / 10 && digit > Integer.MAX_VALUE % 10)) {     
                // If integer overflowed return 2^31-1, otherwise if underflowed return -2^31.    
                return sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE;
            }
            
            // Append current digit to the result.
            result = 10 * result + digit;
            index++;
        }
        
        // We have formed a valid number without any overflow/underflow.
        // Return it after multiplying it with its sign.
        return sign * result;
    }
    
}