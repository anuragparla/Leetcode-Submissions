class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        int[] pFreq = new int[26];
        for(char value : p.toCharArray()) pFreq[value - 'a']++;
        int[] anagramFreq = new int[26];
        List<Integer> result = new ArrayList<>();
        int left = 0, right = 0;
        while(right < s.length()){
            char currentChar = s.charAt(right);
            if(right - left + 1 <= p.length()){
                anagramFreq[currentChar - 'a']++;
                if(Arrays.equals(pFreq, anagramFreq)) result.add(left);
                right++; //expand the window
            }else{
               anagramFreq[s.charAt(left) - 'a']--;
                left++; // shrink the window
            }
        }
        return result;
    }
}