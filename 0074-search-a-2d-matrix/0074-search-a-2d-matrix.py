class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0 or matrix is None:
            return False
        rows, cols = len(matrix), len(matrix[0])
        low = 0
        high = (rows * cols) - 1 

        while low <= high:
            mid = low + (high - low)//2
            rowIndex = mid // cols 
            colIndex = mid % cols 
            if matrix[rowIndex][colIndex] == target:
                return True
            elif matrix[rowIndex][colIndex] > target:
                high = mid - 1 
            else:
                low = mid + 1 
        return False 
