class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        cur=0
        sub=0
        #here we are makiing the first subarray and here we 
        #are going to add if the subarray avg is less than the thrshold
        cur = sum(arr[:k]) 
        if cur/k>=threshold:
            sub+=1


        for r in range(k,len(arr)):
            #so here we need to find the subraay
            cur=cur+arr[r]-arr[r-k]
            if cur/k >= threshold:
                sub+=1
        return sub
            

