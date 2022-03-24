class Solution {
    public String mostCommonWord(String paragraph, String[] banned) {
        Set<String> hs = new HashSet();
        Map<String,Integer> hm = new HashMap();
        int maxFrequency = 0;
        String frequentString ="";
        String[] words = paragraph.split("\\W+");
       
        for(int j = 0; j<banned.length; j++) {
            hs.add(banned[j]);
        }
        for(int i = 0; i<words.length; i++) {
            String word = words[i].toLowerCase();
            if(hm.containsKey(word)){
                System.out.println("word repeated is"+word);
                hm.put(word,hm.get(word)+1);
            }
            else {
                if(!hs.contains(word))
                    hm.put(word,1);
            }
        }
        for(Map.Entry<String, Integer> entry : hm.entrySet()) {
            if(entry.getValue()>maxFrequency) {
                maxFrequency = entry.getValue();
                frequentString = entry.getKey();
            }
        }
        return frequentString;
    }
}