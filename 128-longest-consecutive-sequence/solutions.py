#this is a brute force approach with O(N^3) which results in TLE
class Solution:
    
    def helper(self,arr, curr):
        for i in arr:
            if curr == i:
                return True
        return False
    def longestConsecutive(self, nums: List[int]) -> int:
        longestConsecutive = 0
        currentConsecutive = 0

        for i in nums:
            currentConsecutive +=1 
            currentNum = i 

            while(self.helper(nums,currentNum+1)):
                currentConsecutive +=1
                currentNum +=1 
            longestConsecutive = max(longestConsecutive,currentConsecutive)
            currentConsecutive = 0
        return longestConsecutive
