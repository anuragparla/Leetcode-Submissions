class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        '''
        1st boundary: row < 0 but col is within bounds [ tUP] inc row by 1
        2nd boundary; col < 0 but row is within bounds [tDown] inc col by 1
        3rd boundary: row < 0 and col > len(col) [ tup] inc row by 2 and dec col by 1 
        4th boundary: row >=len(rows) but col in bounds then dec row by 1
        '''
        rows = len(mat)
        cols = len(mat[0])
        res = []
        going_up = True # false meaning we are going down
        i = j = 0

        while len(res) != rows * cols:
            if going_up:

                while i>=0 and j<cols:
                    res.append(mat[i][j])
                    i -=1 
                    j +=1 

                if j == cols:
                        i += 2
                        j -= 1
                elif i < 0:
                    i += 1
                going_up = False
            else:
                while i <rows  and j>=0:
                    res.append(mat[i][j])
                    i +=1 
                    j -=1
                
                if i == rows:
                    j += 2 
                    i -= 1 
                elif j < 0:
                    j +=1 
                
                going_up = True
        
        return res
                


            
            

        