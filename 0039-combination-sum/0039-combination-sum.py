class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0 or candidates is None:
            return []
        self.res = []

        self.recurse(candidates, 0, target, [])
        return self.res
    
    def recurse(self, candidates, idx, target, path):
        if len(candidates) == idx or target < 0:
            return
        if target == 0:
            self.res.append(path[:])
            return
        
        #not choose or 0 case 
        self.recurse(candidates, idx+1, target, path[:])
        #choose or 1 case
        path.append(candidates[idx]) 
        self.recurse(candidates, idx, target-candidates[idx], path[:])

        

        