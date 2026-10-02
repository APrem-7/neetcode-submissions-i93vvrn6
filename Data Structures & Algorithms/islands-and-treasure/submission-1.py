from collections import deque 
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque()
        COL,ROW=len(grid[0]),len(grid)
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]==0:
                    q.append((i,j))
        size=len(q)
        dis=1
        while q:
            for _ in range(size):
                #bfs
                #from here we need to start marking them as 1
                i,j=q.popleft()
                directions=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
                for di,dj in directions:
                    if not (di>=ROW or dj>=COL or di<0 or dj<0 ) and grid[di][dj]==2147483647:
                        grid[di][dj]=dis
                        q.append((di,dj))
                
            dis+=1
            size=len(q)

