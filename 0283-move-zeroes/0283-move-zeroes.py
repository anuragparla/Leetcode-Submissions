class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        if left and right are 0 only inc right
        if left is 0 and right is != 0 swap and inc both pointers 
        '''
        left = 0 
        right = 1 
        if len(nums)> 1:
            while left < len(nums) and right < len(nums):
                if nums[left] == 0 and nums[right] != 0:
                    nums[left],nums[right] = nums[right],nums[left]
                    left +=1 
                    right +=1 
                elif nums[left] == 0 and nums[right] == 0:
                    right += 1
                else:
                    left += 1 
                    right += 1 
                
            
        