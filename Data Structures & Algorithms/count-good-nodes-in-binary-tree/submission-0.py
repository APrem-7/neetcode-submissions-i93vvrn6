# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Intuition
# <!-- So basically what is going on here is that we are going from the root of the binary tree and then from there we are going down the BST  and comapring the node.val with the grewtest element we have seeen till now adn if 
# since the statement says " path from the root of the tree to the node x contains no nodes with a value greater than the value of node x " we have to make sure that no node.val >= maxVal seen till now... if it is gretaer then boom it doesnt qualify as a good node-->

# Approach
# <!-- Step-by-step explanation of how you solve it -->

# Complexity
# - Time complexity:
# <!-- O(n) or whatever applies -->
# - Space complexity:
# <!-- O(n) or whatever applies -->
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def dfs(node,maxVal):
            if not node:
                return 0
            res = 1 if node.val>=maxVal else 0
            maxVal=max(node.val,maxVal)
            res+=dfs(node.left,maxVal)
            res+=dfs(node.right,maxVal)

            return res
        res=dfs(root,root.val)
        return res