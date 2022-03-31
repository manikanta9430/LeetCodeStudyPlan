class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = TreeNode()
        def dfs(root,p,q):
            if root.val > max(p.val,q.val): 
                self.lowestCommonAncestor(root.left,p,q)    # move to left node
            elif root.val < min(p.val,q.val):
                self.lowestCommonAncestor(root.right,p,q)   # move to right node
            elif root.val < max(p.val,q.val) and root.val > min(p.val,q.val):
                self.ans = root                             # if p and q both lies in left and right of root
            elif root.val == p.val or root.val == q.val:    # if p is parent of q or vice versa
                self.ans = root
            return self.ans
        return dfs(root,p,q)
