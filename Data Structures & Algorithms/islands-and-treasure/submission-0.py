class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #so this is a classic mutiple source BFS traversal problem

        ROW,COL=len(grid),len(grid[0])
        q=deque()
        visit=set()
        def addRoom(r,c):
            #now checking if this is a valid grid number
            if r>=ROW or c>=COL or r<0 or c<0 or grid[r][c]==-1:
                return
            if (r,c) in visit:
                return
            visit.add((r,c))
            q.append((r,c))
            

        for i in range(ROW):
            for j in range(COL):
                #so here we are going to iterate thorught the grid to find the sources(Gates)
                if grid[i][j]==0:
                    visit.add((i,j))
                    q.append((i,j))
        
        #so now we are going to perform bfs on our queue
        dist=0
        while q:
            for i in range(len(q)):
                r,c =q.popleft()
                grid[r][c]=dist
               
                #now traverse all adjacent 
                addRoom(r+ 1,c)
                addRoom(r-1,c)
                addRoom(r,c+1)
                addRoom(r,c-1)
            dist+=1
            
