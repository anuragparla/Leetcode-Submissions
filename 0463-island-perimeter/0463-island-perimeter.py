class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visitedSet = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        def dfs(row,col):
            #base case
            if row < 0 or col < 0 or row >=len(grid) or col >=len(grid[0]) or grid[row][col] == 0:
                return 1

            if (row,col) in visitedSet:
                return 0
            visitedSet.add((row,col))
            perimeter = 0
            for coord in directions:
                r , c = coord[0], coord[1]
                perimeter += dfs(row + r, col + c)
            # perimeter = dfs(row, col+1)
            # perimeter += dfs(row, col - 1)
            # perimeter += dfs(row - 1, col)
            # perimeter += dfs(row + 1, col)
            return perimeter
    
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(r,c)


        