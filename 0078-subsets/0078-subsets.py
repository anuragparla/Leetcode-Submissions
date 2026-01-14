class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.output = []
        self.recurse(0,[],nums)
        return self.output
    def recurse(self,idx,res,nums):
        if idx >= len(nums):
            self.output.append(res[:])
            return
        
        #not pick
        self.recurse(idx+1,res,nums)

        #pick
        res.append(nums[idx])
        self.recurse(idx+1,res,nums)
        res.pop()

        