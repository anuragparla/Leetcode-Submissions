import math
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0 
        right = k - 1 
        maxAvg = -math.inf
        sum = 0
        for i in range(left, right+1):
                sum += nums[i]
        while right < len(nums):
            if left>0:
                sum = sum + nums[right] - nums[left -1]
            currAvg = sum/k
            maxAvg = max(maxAvg, currAvg)
            left += 1 
            right += 1 
        return maxAvg