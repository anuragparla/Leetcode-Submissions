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

#using sorting 
class Solution:
    
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        longestConsecutive = 1
        currentConsecutive = 1
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    currentConsecutive +=1
            else:
                longestConsecutive = max(longestConsecutive,currentConsecutive)
                currentConsecutive = 1
        return max(longestConsecutive, currentConsecutive)
    
