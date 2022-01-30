class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll(
          "[^a-zA-Z0-9]", "");
        s = s.toLowerCase();
        System.out.println(s);
        char[] c = s.toCharArray(); 
        int i = 0;
        int j = s.length()-1;
        while(i<j) {
            if(c[i]==c[j]){
                i++;
                j--;
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
    
}