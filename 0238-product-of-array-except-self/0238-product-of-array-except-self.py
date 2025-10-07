class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = 1 
        #prefix product for lhs of an element
        lhs=[1]*len(nums)
        for i in range(1,len(nums)):
            lhs[i] = prefix_product * nums[i-1]
            prefix_product = lhs[i]
        
        #prefix product for lhs of an element
        rhs=[1]*len(nums)
        prefix_product = 1 
        for i in range(len(nums)-2, -1,-1):
            rhs[i] = prefix_product * nums[i+1]
            prefix_product = rhs[i]
        
        for i in range(len(lhs)):
            rhs[i] = lhs[i] * rhs[i]
        
        return rhs

