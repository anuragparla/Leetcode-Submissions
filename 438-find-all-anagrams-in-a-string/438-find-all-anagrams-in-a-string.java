class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> result = new ArrayList();
        if(s.equals(p)) {
            result.add(0);
            return result;
        }
        else if(s.length()<p.length()) {
            return result;
        }
        else {
            Map<Character, Integer> pCount = new HashMap();
            Map<Character,Integer> sCount = new HashMap();
            for(int i = 0; i<p.length();i++) {
                if(pCount.containsKey(p.charAt(i))) {
                    pCount.put(p.charAt(i),(int)(pCount.get(p.charAt(i)) +1));
                }
                else {
                    pCount.put(p.charAt(i),1);
                }
            }
            char[] sArray = s.toCharArray();
            int p1 = 0;
            int p2 = p.length()-1;
            for(int i = p1; i<=p2;i++) {
                if(sCount.containsKey(sArray[i])) {
                    sCount.put(sArray[i],(int)(sCount.get(sArray[i]) +1));
                }
                else {
                    sCount.put(sArray[i],1);
                }
            }
            if(sCount.equals(pCount)) {
                result.add(p1);
            }
            for(int j = p.length(); j<sArray.length;j++) {
                    
                    if(sCount.containsKey(sArray[j])) {
                    sCount.put(sArray[j],(int)(sCount.get(sArray[j]) +1));
                }
                else {
                    sCount.put(sArray[j],1);
                }
               sCount.put(sArray[p1],(int)(sCount.get(sArray[p1])-1));
                if (sCount.get(sArray[p1]) == 0)
                {
                    sCount.remove(sArray[p1]);
                }
                p1+=1;
                if(sCount.equals(pCount)) {
                result.add(p1);
            }
            }
                
            }
                
                
            
            return result;
        }
    }
