class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0 or nums is None:
            return []
        self.res = []
        self.recurse(nums, 0, [])
        return self.res
    
    def recurse(self, nums, idx, path):
        if idx == len(nums):
            self.res.append(path)
            return

        #do not choose or 0 case
        self.recurse(nums, idx+1, path[:])
        path.append(nums[idx])
        #choose or 1 case
        self.recurse(nums, idx+1, path[:])
        
        