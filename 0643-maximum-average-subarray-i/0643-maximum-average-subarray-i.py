class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = float('-inf')
        l = r = 0 
        sum = 0
        while r < len(nums):
            sum += nums[r]
            if (r - l + 1) == k :
                max_avg = max(sum / k, max_avg)
                sum -= nums[l]
                l += 1 
                
            
            r += 1
        return max_avg
            

        