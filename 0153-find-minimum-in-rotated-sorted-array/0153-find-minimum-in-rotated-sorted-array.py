class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        since the array is sorted, rotating the array 
        will result in 2 halfs with each being sorted 
        i.e. 1 half would have larger values and the 
        other would have smaller depending on how many
        times the array has been rotated

        do a regular BS and find the mid. 
        if mid >= left most element then we need to move
        left = mid +1 
        if mid <= left most element then we need to move 
        right = mid - 1 

        PS: this logic will only work for rotated sorted array

        '''
        left, right = 0, len(nums)-1
        minVal = nums[0]
        while left<=right:
            mid = left + (right-left)//2
            if nums[left]<nums[right]:
                minVal = min(minVal, nums[left])
                break
            
            elif nums[mid] >=nums[left]:
                minVal = min(minVal, nums[mid])
                left = mid +1 
            else:
                minVal = min(minVal, nums[mid])
                right = mid -1 
        return minVal
        

        