class Solution:
    def dp(self, root, lookup):
        if not root:
            return 0
        
        if root not in lookup:
            rootTaken = root.val
            if root.left:
                rootTaken += self.dp(root.left.left, lookup) + self.dp(root.left.right, lookup)
            if root.right:
                rootTaken += self.dp(root.right.left, lookup) + self.dp(root.right.right, lookup)

            rootNotTaken = self.dp(root.left, lookup) + self.dp(root.right, lookup)
            
            lookup[root] = max(rootTaken, rootNotTaken)

        return lookup[root]
        
    def rob(self, root: TreeNode) -> int:
        return self.dp(root, {})
