class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxlocal = [[0] * (n-2) for _ in range((n-2))]

        for i in range(len(maxlocal)):
            for j in range(len(maxlocal[0])):
                max_val = 0
                center = grid[i+1][j+1]
                for k in range(i,i+3):
                    for l in range(j,j+3):
                        if grid[k][l] > max_val:
                            max_val = grid[k][l]
                maxlocal[i][j] = max_val
        return maxlocal
        