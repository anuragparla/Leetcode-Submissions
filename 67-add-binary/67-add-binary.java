class Solution {
    public String addBinary(String a, String b) {
        int carry = 0;
        StringBuilder res  = new StringBuilder();
        int i = a.length() - 1;
        int j = b.length() - 1;
        int num1 = 0;
        int num2 = 0;
        int sum = 0;
        while(i >= 0 || j >= 0) {
            if(i < 0) {
                num1 = 0;
            }
            else {
                 num1 = (int)a.charAt(i) - (int)'0';
            }
            if( j < 0) {
                num2 = 0;
            }
            else {
                num2 = (int) b.charAt(j) - (int)'0';
            }
            sum = num1+num2+carry;
            res.append(sum % 2);
            carry = sum / 2;
            i -= 1;
            j -= 1;
           
            
        }
        if(carry != 0)
            res.append(carry);
        return res.reverse().toString();
    }
}