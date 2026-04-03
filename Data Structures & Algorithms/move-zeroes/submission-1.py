class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left=0


        while nums[left]!=0:
            left+=1
            if left==len(nums):
                return nums
           
        
        for right in range(left,len(nums)):
            if nums[left]!=0:
                left+=1
            if nums[right]!=0:
                #then this must be moved to left
                nums[left]=nums[right]
                nums[right]=0
        return nums
        
        