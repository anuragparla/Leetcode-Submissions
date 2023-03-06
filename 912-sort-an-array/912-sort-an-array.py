class Solution(object):
    
    def merge(self,left, right):
        leftIndex = 0
        rightIndex = 0
        res = []
        while leftIndex<len(left) and rightIndex <len(right):
            if left[leftIndex]<right[rightIndex]:
                res.append(left[leftIndex])
                leftIndex +=1
            else:
                res.append(right[rightIndex])
                rightIndex +=1 
        res.extend(left[leftIndex:])
        res.extend(right[rightIndex:])
        return res


    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums 
        length = len(nums)//2
        left = self.sortArray(nums[:length])
        right = self.sortArray(nums[length:])
        return self.merge(left,right)
