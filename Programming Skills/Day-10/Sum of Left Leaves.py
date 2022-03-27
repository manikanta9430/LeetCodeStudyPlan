class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def bfs(n1, path, side):
            if n1:
                if not n1.right and not n1.left and side == 1:
                    self.res.append(path+[n1.val])
                if n1.left:
                    bfs(n1.left, path, 1)
                if n1.right:
                    bfs(n1.right, path, -1)
        self.res = []
        bfs(root,[], 0)
        return sum(sum(self.res, []))
