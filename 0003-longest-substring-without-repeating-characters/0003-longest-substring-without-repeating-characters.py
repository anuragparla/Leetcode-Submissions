class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        time: o(N)
        space: O(N)
        need a set to keep track of duplicate chars
        need a max_length
        need left and right ptrs for variable sliding window
        '''
        left, right = 0,0
        track_unique_chars = set()
        max_length = 0

        if not s:
            return 0
        while right < len(s):
            while s[right] in track_unique_chars:
                track_unique_chars.remove(s[left])
                left += 1 
            track_unique_chars.add(s[right])
            max_length = max(max_length, right - left + 1)
            right += 1
        
        return max_length


        