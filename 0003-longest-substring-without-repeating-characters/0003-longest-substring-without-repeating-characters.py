class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Variable window problem
        we need to keep left and right as start and end for the window
        since this problem asks us not have duplicates, i will use a 
        set to keep track of duplicates 
        initially both left and right start from 0 
        hence window size can be calculated as (right - left) + 1 
        perform a max on that to return the longest 
        it gets tricky when right pointer points to a character in the set 
        then you need to move the left pointer and everytime it moves 
        remove its corresponding element till s[r] is not in the set 
        when it isn't it will be the updated end point of the window and now 
        add that to the set and continue till r goes out of bounds 
        Time: O(n)
        Space: O(n) as in a string with unique chars, all n chars will be 
        stored 
        '''
        left, right = 0, 0 
        longestSubString = 0
        trackDuplicates = set()
        while right<len(s):
            while s[right] in trackDuplicates:
                trackDuplicates.remove(s[left])
                left += 1 
            currWindowSize = (right-left) + 1 
            longestSubString = max(longestSubString,currWindowSize )
            trackDuplicates.add(s[right])
            right += 1 
        return longestSubString


       
