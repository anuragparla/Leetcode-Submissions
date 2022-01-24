class Solution {
    public boolean detectCapitalUse(String word) {
        int uppercaseCount = 0 ; 
        int lowercaseCount = 0 ;
        int stringLength = word.length();
        for ( int i = 0 ; i<stringLength; i++) {
            if ((int)word.charAt(i) >= 65 && (int)word.charAt(i) <=90){
                uppercaseCount += 1;
            }
            else if ((int)word.charAt(i) >= 97 && (int)word.charAt(i) <=122)
            {
                lowercaseCount +=1;
            }
        }
        if(uppercaseCount == word.length() || lowercaseCount == word.length())
            return true;
        else if(uppercaseCount == 1 && Character.isUpperCase(word.charAt(0)))
        {
            return true;
        }
            
        return false;
    }
}