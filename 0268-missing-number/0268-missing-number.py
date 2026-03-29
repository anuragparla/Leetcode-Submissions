class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = n * (n + 1) // 2 
        sum_of_inputs = 0 
        for i in nums:
            sum_of_inputs += i 
        return total_sum - sum_of_inputs
        