class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if len(nums) == 0 or nums is None:
            return []
        self.res = []
        self.backtrack(nums, 0, [])
        return self.res
    
    def backtrack(self, nums, idx, path):
        if idx == len(nums):
            print('when base case')
            print(path)
            self.res.append(path[:])
            return

        #do not choose or 0 case
        self.backtrack(nums, idx+1, path)
        path.append(nums[idx])
        print('after append')
        print(path)
        #choose or 1 case
        self.backtrack(nums, idx+1, path)
        path.pop()
        print('after pop')
        print(path)
        
        