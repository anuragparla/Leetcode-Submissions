class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l = len(nums)
        # prefix = [1]*l
        # suffix = [1]*l 
        # answer = [1]*l
        # prefPlaceHolder = 1 
        # suffPlaceHolder = 1 
        # for i in range(0,len(nums)):
        #     prefix[i] = prefPlaceHolder
        #     prefPlaceHolder *= nums[i]
        
        # for j in range(len(nums)-1, -1, -1):
        #     suffix[j] = suffPlaceHolder
        #     suffPlaceHolder *= nums[j]

        # for k in range(len(nums)):
        #     answer[k] = prefix[k] * suffix[k]
        
        # return answer

        '''
        Optimized approach:
        Since output array is not considered as extra memory, let's store the 
        prefix product in the output array and modify the input array to store 
        the suffix.
        Finally multiply both the arrays and store the result in the output array aka prefix product array
        ex for input [ 1,2,3,4]
        [1,1,2,6] -> o/p aka prefix
        [24,12,4,1] -> modify the input array to make it suffix 
        multiply both to get the result -> [24,12,8,6]
        Time: O(n)
        Space: O(1)
        '''
        result_prefix = [1] * len(nums)

        #calculate prefix 
        prefix = 1 
        for i in range(1,len(nums)):
            prefix *= nums[i-1]
            result_prefix[i] = prefix
        print(result_prefix)
        
        #calculate postfix and store the result in the result_prefix array 
        postfix = 1 
        for i in range(len(nums)-2,-1,-1):
            postfix *= nums[i+1]   
            result_prefix[i] = result_prefix[i] * postfix
        
        return result_prefix

            





    
        


