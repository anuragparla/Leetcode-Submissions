class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_wrd_lngth = 0
        s = s.rstrip()
        for i in range((len(s)-1),-1,-1):
            if s[i] == ' ':
                break
            last_wrd_lngth += 1
        return last_wrd_lngth
        

        