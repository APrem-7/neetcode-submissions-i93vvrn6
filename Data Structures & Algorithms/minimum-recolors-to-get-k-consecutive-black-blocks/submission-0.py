class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #so i need to find the window with the minimum whites here
        whites=0
        ans=float("inf")
        for r in range(k):
            if blocks[r]=="W":
                whites+=1 
        ans = min(whites, ans)  
        #now we got the base here
        #so this is the initial window 
        for r in range(k,len(blocks)):
            if blocks[r]=="W":
                whites+=1
            if blocks[r - k] == 'W':
                whites -= 1
            ans=min(whites,ans)            
        return ans