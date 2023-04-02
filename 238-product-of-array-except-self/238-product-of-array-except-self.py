class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        prefix = [1]*l
        suffix = [1]*l 
        answer = [1]*l
        prefPlaceHolder = 1 
        suffPlaceHolder = 1 
        for i in range(0,len(nums)):
            prefix[i] = prefPlaceHolder
            prefPlaceHolder *= nums[i]
        
        for j in range(len(nums)-1, -1, -1):
            suffix[j] = suffPlaceHolder
            suffPlaceHolder *= nums[j]

        for k in range(len(nums)):
            answer[k] = prefix[k] * suffix[k]
        
        return answer
    
