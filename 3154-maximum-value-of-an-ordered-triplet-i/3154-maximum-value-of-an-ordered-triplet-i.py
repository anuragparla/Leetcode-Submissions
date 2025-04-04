class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxx = float('-inf')
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    maxx = max(maxx, (nums[i]-nums[j])*nums[k])
        if maxx < 0:
            return 0
        return maxx


        