class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates is None or len(candidates) == 0:
            return
        self.res = []
        self.recurse(candidates, target, 0, [])
        return self.res
    
    def recurse(self, candidates, target, idx, path):
        if target < 0 :
            return
        if target == 0:
            self.res.append(path[:])

        #logic
        for i in range(idx, len(candidates)):
           
            path.append(candidates[i])
            self.recurse(candidates, target-candidates[i], i, path)
            path.pop()