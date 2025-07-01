class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
     anagram_map = dict([])
     for i in strs:
        sorted_word = sorted(i)
        key = "".join(sorted_word)
        if key not in anagram_map:
            anagram_map[key] = [i]
        else:
            anagram_map.get(key).append(i)
     
     res = list(anagram_map.values())
     return res 


            