class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        l = len(nums)
        for i in range(l-n):
            res.append(nums[i])
            res.append(nums[i+n])
        return res
        