class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l = r = 0 
        freq_ct_p = dict()
        freq_ct_s = dict()
        res = []
        for ch in p:
             freq_ct_p[ch] =  freq_ct_p.get(ch,0) + 1
        while r < len(s):
            freq_ct_s[s[r]] = freq_ct_s.get(s[r],0) + 1
            if (r - l + 1) == len(p):
                if freq_ct_s == freq_ct_p:
                    res.append(l)
                if s[l] in freq_ct_s:
                    freq_ct_s[s[l]] -= 1 
                    if freq_ct_s[s[l]] == 0:
                        del freq_ct_s[s[l]]
                l += 1
            r += 1
        return res
        
         

        
        