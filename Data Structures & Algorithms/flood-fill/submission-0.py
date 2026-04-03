class Solution:
    def floodFill(self, image, sr, sc, color):
        og_color = image[sr][sc]

        if og_color == color:
            return image

        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(image) or j >= len(image[0]):
                return
            if image[i][j] != og_color:
                return

            image[i][j] = color

            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

        dfs(sr, sc)
        return image
        