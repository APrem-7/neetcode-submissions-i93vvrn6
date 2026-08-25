class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        #so i must check if this particulary is going to wokr in my chip or not
        def weight_works(min_w):
            curr=0
            count=0
            for weight in weights:
                if curr+weight<=min_w:
                    curr+=weight
                else:
                    curr=weight
                    count+=1
            return count+1<=days
        l=max(weights)
        r=sum(weights)

        while l<r:
            mid = l + (r - l) // 2
            if weight_works(mid):
                r=mid
            else:
                l=mid+1
        return l


                    