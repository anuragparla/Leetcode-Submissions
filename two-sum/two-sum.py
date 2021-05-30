class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = 0
        
        if len(nums)<3:
            sum = nums[0]+nums[1]
            if sum == target:
                return [0,1]
        else:
            for i in range(len(nums)):
                diff = target -nums[i]
                if diff in nums and nums.index(diff)!=i:
                    return [i,nums.index(diff)]
            
        
                
    
                
            
            
            
        