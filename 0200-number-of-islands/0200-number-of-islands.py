from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_set = set()
        queue = deque()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        number_of_islands = 0 

        def bfs(row,col):
            queue.append((row,col))
            visited_set.add((row,col))
            
            while queue:
                r, c = queue.popleft()
                for dr , dc in directions:
                    row = dr + r 
                    col = dc + c 
                    if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                        continue
                    if grid[row][col] == "1" and (row,col) not in visited_set:
                        visited_set.add((row,col))
                        queue.append((row,col))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visited_set:
                    bfs(r,c)
                    number_of_islands += 1 
        return number_of_islands


                    


        