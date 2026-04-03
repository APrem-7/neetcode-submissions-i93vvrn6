# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def dfs(root,sume,low,high):
            if not root:
                return sume
            if low <= root.val <= high:
                #found
                sume+=root.val
             
            sume = dfs(root.left, sume, low, high)
            sume = dfs(root.right, sume, low, high)
            
            return sume
        return dfs(root,0,low,high)