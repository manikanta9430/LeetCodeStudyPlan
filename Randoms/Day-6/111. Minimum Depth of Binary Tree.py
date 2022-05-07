class Solution:
    def minDepth(self, root: Optional[TreeNode], depth=1) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        mindepth = float('inf')
        if root.left:
            depth_left = self.minDepth(root.left, depth=depth+1)
            mindepth = min(depth_left, mindepth)
        if root.right:
            depth_right = self.minDepth(root.right, depth=depth+1)
            mindepth = min(depth_right, mindepth)
        return mindepth+1
