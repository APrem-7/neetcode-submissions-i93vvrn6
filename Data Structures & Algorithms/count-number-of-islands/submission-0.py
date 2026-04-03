class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        best=0
        ROW,COLS=len(grid),len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= ROW or j >= COLS:
                return False
            if (i,j) in visit or grid[i][j]=="0":
                return False
            visit.add((i,j))  
            if grid[i][j]=="1":  
                dfs(i, j+1)
                dfs(i, j-1)
                dfs(i+1, j)
                dfs(i-1, j)
                return True
        islands=0
        for i in range(ROW):
            for j in range(COLS):
                if grid[i][j]=="1" and (i,j) not in visit:
                    dfs(i,j)
                    islands+=1
        return islands