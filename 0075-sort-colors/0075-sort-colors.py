class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        temp = [0] * 3
        # stroing frequency
        for i in nums:
            temp[i] = temp[i] + 1
        # computing cumulative sum
        for i in range(1,len(temp)):
            temp[i] = temp[i-1] + temp[i]
        # move the sum values by an index forward
        for i in range((len(temp) - 1),0,-1):
            temp[i] = temp[i-1]
        temp[0] = 0 
        # at this point we know that starting indexes of every number in the range
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[temp[nums[i]]] = nums[i]
            temp[nums[i]] += 1
        
        nums[:] = res
        




