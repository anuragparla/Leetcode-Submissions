class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_count_p = {}
        freq_count_substr = {}
        left = 0
        right = 0
        res = []
        windw_length = len(p) 
        for c in p:
            freq_count_p[c] = freq_count_p.get(c,0) + 1 
        while right < len(s):
            freq_count_substr[s[right]] = freq_count_substr.get(s[right],0) + 1
            if right - left + 1 == windw_length:
                if freq_count_p == freq_count_substr:
                    res.append(left)
                freq_count_substr[s[left]] -= 1
                if freq_count_substr[s[left]] == 0:
                    del freq_count_substr[s[left]]
                left += 1 
            right += 1 
        return res