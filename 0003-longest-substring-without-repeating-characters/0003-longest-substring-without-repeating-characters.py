class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        check_duplicate = set()
        left , right = 0,0
        max_len = 0
        while right < len(s):
            if s[right] not in check_duplicate:
                check_duplicate.add(s[right])
                right += 1 
                max_len = max((right - left),max_len)
                
            else:
                while s[right] in check_duplicate:
                    check_duplicate.discard(s[left])
                    left += 1
        
        return max_len 



        