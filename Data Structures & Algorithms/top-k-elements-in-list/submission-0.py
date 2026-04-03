class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) Count frequencies
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # 2) Buckets: index = frequency, value = list of numbers
        # max frequency can be at most len(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, f in freq.items():
            buckets[f].append(num)
        
        # 3) Go from highest frequency to lowest,
        #    collect elements until we have k
        res = []
        for f in range(len(nums), 0, -1):
            if buckets[f]:
                for num in buckets[f]:
                    res.append(num)
                    if len(res) == k:
                        return res