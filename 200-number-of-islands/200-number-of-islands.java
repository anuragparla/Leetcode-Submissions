class Solution {
    private void dfs(char[][] grid, int row, int col) {
        int nr = grid.length;
        int nc = grid[0].length;
        int r = row;
        int c = col;
        if(r>=nr || c>=nc || r<0 || c<0||grid[r][c] == '0')
            return;
        if(grid[r][c] == '1')
            grid[r][c] = '0';
        dfs(grid,r,c-1);
        dfs(grid,r,c+1);
        dfs(grid,r+1,c);
        dfs(grid,r-1,c);
    
    }
    public int numIslands(char[][] grid) {
        int nr = grid.length;
        int nc = grid[0].length;
        int nIslands = 0;
        
        for(int i = 0 ; i<nr;i++) {
            for(int j = 0; j<nc;j++) {
                if(grid[i][j] == '1')
                    nIslands +=1 ;
                    dfs(grid,i,j);
            }
        }
        return nIslands;
    }
}