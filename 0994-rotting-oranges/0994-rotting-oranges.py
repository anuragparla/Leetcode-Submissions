from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time, fresh_oranges = 0, 0
        rows, cols = len(grid), len(grid[0])

        #counting fresh oranges and initializing the queue with rotting oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_oranges += 1 
                elif grid[r][c] == 2:
                    queue.append([r,c])
        
        #directions list
        directions = [[0,1],[0,-1],[1,0],[-1,0]]

        #bfs
        while queue and fresh_oranges > 0:
            #in traditional bfs we directly pop from the queue since we will have
            #only one node at level 0 but that's not the case here
            for idx in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    row = dr + r 
                    col = dc + c

                    if (row < 0 or row == len(grid) or 
                    col < 0 or col == len(grid[0]) or 
                    grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    queue.append([row,col])
                    fresh_oranges -= 1
            time += 1
        return time if fresh_oranges == 0 else -1  


        