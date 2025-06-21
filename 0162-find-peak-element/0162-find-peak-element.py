class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peak_element = float('-inf')
        peak_element_index = 0

        left, right = 0, len(nums) - 1
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0]>nums[1] else 1
        while left<right:
            mid = left + (right-left)//2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left
            

        