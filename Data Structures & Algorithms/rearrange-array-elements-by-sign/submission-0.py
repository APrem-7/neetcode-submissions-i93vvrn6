class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos=[]
        neg=[]
        res=[]
        for i in nums:
            if i<=0:
                neg.append(i)
            else:
                pos.append(i)
        merged=pos+neg

        l,r=0,len(pos)
        while l<len(pos) and r<len(merged):
            res.append(merged[l])
            l+=1
            res.append(merged[r])
            r+=1
        return res

