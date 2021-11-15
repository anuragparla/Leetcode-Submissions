class Solution {
    /**
    The below solution is using leetcode's algo to convert a 2D array to 1D and vice versa
    **/
    /*
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        int m = mat.length, n = 0;
        for(int i=0;i<1;i++){
            n = mat[i].length;
        }
        if ((m*n) !=(r*c)){
            return mat;
        }
        else{
            int[] temp = new int[r*c];
            for(int i=0;i<m;i++){
                for(int j=0;j<n;j++){
                    temp[n*i+j] = mat[i][j];
                }
            }
            
            int[][] res = new int[r][c];
            for(int i=0;i<temp.length;i++){
                res[i/c][i%c] = temp[i];
            }
            return res;
        }
        //return mat;
    }
}*/

//converts 2D to 1D array
    private static int[] formOneDArray(int[][] a, int row, int col)
    {
        int oned[] = new int[row*col];
        int p = 0;
        for(int i = 0; i < row; i++)
        {
            for(int j = 0; j < col; j++)
                oned[p++] = a[i][j];
        }
        
        return oned;
    }
    
   //converts 1D to 2D array
    private static int[][] formTwoDArray(int[] a, int r, int c)
    {
        int ans[][] = new int[r][c];
        int p = 0;
        for(int i = 0; i < r; i++)
        {
            for(int j = 0; j < c; j++)
                ans[i][j] = a[p++];
        }
        
        return ans;
    }
    public int[][] matrixReshape(int[][] mat, int r, int c) {
        
        int row = mat.length;
        int col = mat[0].length;
        
        //if original number of rows and columns are equal to r and c
        if( row == r && col == c)
            return mat; //original matrix is returned
        //if the count of elements are different
       else if( row * col != r * c )
            return mat; //original matrix is returned
        else
        {
            int ans[][] = new int[r][c]; //answer array
            //convert given matrix to one D array
            int a[] = formOneDArray(mat, row, col); 
            //convert one D array to 2 D array
            ans = formTwoDArray(a, r, c);
            return ans; //return ans
            
        }
    }
}
