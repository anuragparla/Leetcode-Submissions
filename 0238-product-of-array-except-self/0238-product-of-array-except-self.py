class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
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
        '''
        #optimzied solution 
        res = [1] * len(nums)
        prefix_product = 1 
        # calculate the products on LHS
        for i in range(1,len(nums)):
            res[i] = nums[i-1] * prefix_product
            prefix_product = res[i]
        prefix_product = 1 
        # use result array and modify it for rhs prod calc
        for j in range(len(nums)-2, -1,-1):
            res[j] = res[j] * nums[j+1] * prefix_product
            prefix_product = nums[j+1] * prefix_product
        return res
