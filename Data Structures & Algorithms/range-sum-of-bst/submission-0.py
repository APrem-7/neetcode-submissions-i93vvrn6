class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        
        def root_func(root, sume, low, high):
            if not root:
                return sume
            
            if low <= root.val <= high:
                sume += root.val
             
            sume = root_func(root.left, sume, low, high)
            sume = root_func(root.right, sume, low, high)
            
            return sume
        
        return root_func(root, 0, low, high)