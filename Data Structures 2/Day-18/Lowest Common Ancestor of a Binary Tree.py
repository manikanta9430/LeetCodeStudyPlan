import functools

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.output = root

        def commonAncestor(root, p, q):
            if root:
                return isIn(p, root) and isIn(q, root)
            else:
                return False

        @functools.lru_cache(maxsize=None)
        def isIn(p, root):
            if root:
                if root == p:
                    return True
                else:
                    return isIn(p, root.left) or isIn(p, root.right)
            else:
                return False

        def dfs(root, p, q):
            if commonAncestor(root.left, p, q):
                self.output = root.left
                dfs(root.left, p, q)
            elif commonAncestor(root.right, p, q):
                self.output = root.right
                dfs(root.right, p, q)

        dfs(root, p, q)
        return self.output

