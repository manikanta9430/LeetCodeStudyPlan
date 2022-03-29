class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.res = False
        
        def dfs(root, sm):
            sm += root.val

            if root.left:
                dfs(root.left, sm)
            if root.right:
                dfs(root.right, sm)

            if not root.left and not root.right and sm == targetSum:
                self.res = True

        if not root:
            return 0
        
        dfs(root, 0)
        
        return self.res
