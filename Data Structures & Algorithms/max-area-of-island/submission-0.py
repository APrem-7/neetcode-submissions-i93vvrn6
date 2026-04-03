class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visit=set()
        best=0
        ROW,COLS=len(grid),len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROW or j >= COLS:
                return 0
            if (i,j) in visit or grid[i][j]==0:
                return 0
            visit.add((i,j))  
            if grid[i][j]==1:  
                return(1
                + dfs(i, j+1)
                + dfs(i, j-1)
                + dfs(i+1, j)
                +dfs(i-1, j))
                return area


        for i in range(ROW):
            for j in range(COLS):
                if grid[i][j]==1 and (i,j) not in visit:
                    area=dfs(i,j)
                    best=max(area,best)
        return best