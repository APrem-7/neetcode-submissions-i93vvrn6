class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        og_color=image[sr][sc]
        visit=set()
        def dfs(i,j):
            if (i,j) in visit:
                return
            if i>=len(image) or j>=len(image[0]) or i<0 or j<0:
                return
            if image[i][j]!=og_color:
                return
            
            visit.add((i,j))
            
            image[i][j]=color
            dfs(i,j+1)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i-1,j)

           
        dfs(sr,sc)
        return image