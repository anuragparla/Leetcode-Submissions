class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_map_p = dict()
        for chr in p:
            freq_map_p[chr] = freq_map_p.get(chr,0)+1
        freq_map_window = {}
        left , right = 0,0
        k = len(p)
        res = []
        while right < len(s):
            freq_map_window[s[right]] = freq_map_window.get(s[right],0) + 1 
            if right - left + 1 == k:
                if freq_map_window == freq_map_p: 
                    res.append(left)
                freq_map_window[s[left]] -= 1
                if freq_map_window[s[left]] == 0:
                    del freq_map_window[s[left]]
                left += 1 
            right += 1 
        return res
        