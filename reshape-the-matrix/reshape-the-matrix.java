class Solution {
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
            /*
            for(int i=0;i<temp.length;i++){
            System.out.println(temp[i]);
            }*/
            int[][] res = new int[r][c];
            for(int i=0;i<temp.length;i++){
                res[i/c][i%c] = temp[i];
            }
            return res;
        }
        //return mat;
    }
}