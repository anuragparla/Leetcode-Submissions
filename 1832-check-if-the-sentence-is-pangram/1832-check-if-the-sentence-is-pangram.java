class Solution {
    public boolean checkIfPangram(String sentence) {
        Map<Character,Integer> hm = new HashMap<>();
        for(int i = 0; i<sentence.length();i++) {
            if(hm.containsKey(sentence.charAt(i))){
                hm.put(sentence.charAt(i),hm.get(sentence.charAt(i))+1);
            }
            else{
                hm.put(sentence.charAt(i),1);
            }
        }
        if(hm.size() == 26)
            return true;
    return false;
}
}