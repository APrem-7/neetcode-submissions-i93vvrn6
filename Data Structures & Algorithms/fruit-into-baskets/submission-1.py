from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        hm=defaultdict(int)
        left=0
        best=0
        total=0

        for i in range(len(fruits)):
            hm[fruits[i]] += 1
            total+=1
            while len(hm)>2:
                hm[fruits[left]]-=1
                total-=1
                if not hm[fruits[left]]:
                    del hm[fruits[left]]
                left+=1
            best=max(total,best)
                
        return best