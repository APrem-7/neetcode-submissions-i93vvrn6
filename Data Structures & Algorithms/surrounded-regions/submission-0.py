class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW,COL=len(board),len(board[0])
        def dfs(r,c):
            if r>=ROW or c>=COL or r<0 or c<0:
                return 
            if board[r][c] != 'O':
                return
            board[r][c]="T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)  

            return board

        for c in range(COL):
            #top
            dfs(0,c)
            #bottom
            dfs(ROW-1,c)
        for r in range(ROW):
            #left
            dfs(r,0)
            #right
            dfs(r,COL-1)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j]!="T" and board[i][j]=="O":
                    #then we mark it as X
                    board[i][j]="X"
        for i in range(ROW):
            for j in range(COL):
                if board[i][j]=="T" :
                    #then we mark it as O
                    board[i][j]="O"

