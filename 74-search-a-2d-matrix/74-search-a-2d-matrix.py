class Solution(object):
    def binarySearch(self,matrix, target):
        if len(matrix) == 0:
            return False
        start = 0
        end = len(matrix)
        mid = (start + (end-start) ) // 2 
        if matrix[mid] == target:
            return True
        elif matrix[mid] < target:
            return self.binarySearch(matrix[mid+1 :], target)
        else:
            return self.binarySearch(matrix[:mid],target)


    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            res = self.binarySearch(i,target)
            if res:
                return True
        return False
