class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHashMap={}

        for i in range(len(nums)):

            result=target-nums[i]
            if (result in numsHashMap):
                return [ numsHashMap[result],i ]
        
            numsHashMap[nums[i]]=i
    