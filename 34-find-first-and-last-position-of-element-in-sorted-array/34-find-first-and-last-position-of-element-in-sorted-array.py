class Solution:
    def binSearch(self,nums,target,leftBiase):
        lp = 0
        rp = len(nums)-1
        mid = 0
        index = -1
        while lp<=rp:
            mid = (lp+rp)//2
            if(nums[mid] == target):
                index=mid
                if(leftBiase):
                    rp = mid-1
                else:
                    lp=mid+1
            elif(nums[mid]>target):
                rp=mid-1
            elif(nums[mid]<target):
                lp=mid+1
        return index
    
    
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        left = self.binSearch(nums,target,True)
        right = self.binSearch(nums,target,False)
        
        return [left,right]
    
    
        
        