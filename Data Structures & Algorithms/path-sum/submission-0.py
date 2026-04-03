# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,current_number,targetSum):
            if not node:
                return False
            current_number +=  node.val
            if not node.left and not node.right:
                if current_number==targetSum:
                    return True
                
            return dfs(node.left,current_number,targetSum) or dfs(node.right,current_number,targetSum)
            
        return dfs(root,0,targetSum)
        return False

