class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0,0
        freq_count = {}
        longest_substr = 0 
        while right < len(s):
            freq_count[s[right]] = freq_count.get(s[right],0)+ 1
            max_count = max(freq_count.values())
            substr_length = right - left + 1 
            if substr_length - max_count <= k:
                longest_substr = max(longest_substr, substr_length)
                right += 1 
            else:
                freq_count[s[left]] -= 1
                freq_count[s[right]] -= 1 
                if freq_count[s[left]] == 0:
                    del freq_count[s[left]]
                # if freq_count[s[right]]== 0:
                #     del freq_count
                left += 1 
        return longest_substr
