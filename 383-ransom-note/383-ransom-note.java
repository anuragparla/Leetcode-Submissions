import java.util.*;
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        /*
        ransomNote from magazine [ possible / not ]
        */
        Hashtable<Character,Integer> ransomString = new Hashtable<>();
        Hashtable<Character,Integer> magazineString = new Hashtable<>();
        
        for(int i = 0 ; i<ransomNote.length(); i++) {
            if(ransomString.containsKey(ransomNote.charAt(i))) {
                ransomString.put(ransomNote.charAt(i),ransomString.get(ransomNote.charAt(i)) +1);
            }
            else {
                ransomString.put(ransomNote.charAt(i),1);
            }   
        }
        for(int j = 0; j<magazine.length(); j++) {
            if(magazineString.containsKey(magazine.charAt(j))) {
                magazineString.put(magazine.charAt(j),magazineString.get(magazine.charAt(j)) +1);
            }
            else {
                magazineString.put(magazine.charAt(j),1);
            }  
        }
        System.out.println(ransomString);
        System.out.println(magazineString);
        for(int k = 0; k<ransomNote.length(); k++) {
            char keyToSearch = ransomNote.charAt(k);
            if(magazineString.containsKey(keyToSearch))
            {
                if(ransomString.get(keyToSearch) > magazineString.get(keyToSearch))
                return false;
            }
            else 
                return false;
            
        }
        return true;
    }
}