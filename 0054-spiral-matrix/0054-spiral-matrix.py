class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        '''
        step 1: scan first row 
        step 2: scan last col 
        step 3: scan last row 
        step 4: scan first col 
        step 5: first row count +1 , last col -1 last row -1, first col + 1 
        '''
        rows = len(matrix)
        cols = len(matrix[0])
        rows, cols = len(matrix), len(matrix[0])
        top, bottom = 0, rows - 1
        left, right = 0, cols - 1
        traversed_elements = []
        while top<=bottom and left<=right:
            for i in range(left, right+1):
                traversed_elements.append(matrix[top][i])
            top += 1 
            if top<=bottom:
                for i in range(top, bottom +1):
                    traversed_elements.append(matrix[i][right])
                right -= 1
            if left<=right and top <= bottom :
                for i in range(right, left-1, -1):
                    traversed_elements.append(matrix[bottom][i])
                bottom -= 1
            if top <= bottom and left<=right:
                for i in range(bottom, top -1, -1):
                    traversed_elements.append(matrix[i][left])
                left += 1
        return traversed_elements

        

        