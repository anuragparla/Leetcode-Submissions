class Solution {
    public String convertToTitle(int columnNumber) {
        int base = 26;
        StringBuilder sb = new StringBuilder();
        while (columnNumber !=0 ) {
            int rem = columnNumber % base;
            if (rem != 0) {
                sb.append((char)('A' + rem -1));
            }
            else {
                sb.append('Z');
                columnNumber --;
            }
            
            columnNumber /= base;
        }
        return sb.reverse().toString();
    }
}