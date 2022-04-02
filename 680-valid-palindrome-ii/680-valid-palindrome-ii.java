class Solution {
    
    private boolean isPalindrome(String s, int l, int r) {
        while(l<r){
            if(s.charAt(l) != s.charAt(r))
                return false;
            l +=1;
            r -=1;
        }
        return true;
    }
    public boolean validPalindrome(String s) {
        int lp = 0;
        int rp = s.length()-1;
        while(lp<rp) {
            if(s.charAt(lp) != s.charAt(rp)) {
                return (isPalindrome(s,lp,rp-1) || isPalindrome(s,lp+1,rp));
            }
            lp +=1;
            rp -=1;
        }
        return true;
        
    }
}