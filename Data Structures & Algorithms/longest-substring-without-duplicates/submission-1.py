class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm =collections.defaultdict(int)

        total,left,best=0,0,0

        for i in range(len(s)):
        #addthe the thing in the set
            hm[s[i]]+=1
            total+=1
            while hm[s[i]]>1:
                hm[s[left]]-=1
                left+=1
                total-=1
                
            best=max(total,best)
        return best