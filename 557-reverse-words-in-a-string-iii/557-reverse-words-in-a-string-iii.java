class Solution {
    public String reverseWords(String s) {
        String[] ss = s.split(" ");
        
        //for(int i = 0; i<ss.length(); i++) {
        int p1 = 0 ;
        int p2 = 0;
        for(int i = 0; i<ss.length; i++){
            char[] c = ss[i].toCharArray();
            p2 = c.length -1;
            while(p1<=p2) {
                char temp = c[p1];
                c[p1++] = c[p2];
                c[p2--] = temp;
            }
            ss[i] = new String(c);
            p1 = 0 ;
            p2 = 0;
        }
        
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i<ss.length; i++) {
            sb.append(ss[i]);
            if(i<ss.length-1)sb.append(" ");
        }
        return sb.toString();
            
       // }
    }
}