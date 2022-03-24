import java.util.*;
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //approach one 
        /*
        Map<String,List<String>> hm = new HashMap<>();
        List<List<String>> res = new ArrayList<>();
        for(int i = 0; i<strs.length; i++) {
            char[] temp = strs[i].toCharArray();
            Arrays.sort(temp);
            String k = new String(temp);
            if(hm.containsKey(k))
                hm.get(k).add(strs[i]);
            else
                hm.put(k,new ArrayList(Arrays.asList(strs[i])));
        }
        for(List<String> val:hm.values()) {
            res.add(val);
        } 
        return res;*/
        Map<String,List<String>> hm = new HashMap<>();
        List<List<String>> res = new ArrayList<>();
        for(int i = 0; i<strs.length; i++) {
            int[] count = new int[26];
            for(int j = 0; j<strs[i].length(); j++) {
                count[strs[i].charAt(j)-97] += 1;
            }
            String k = Arrays.toString(count);
            if(hm.containsKey(k))
                hm.get(k).add(strs[i]);
            else
                hm.put(k,new ArrayList(Arrays.asList(strs[i])));
        }
        for(List<String> val : hm.values()) {
            res.add(val);
        }
        return res;
    }
}