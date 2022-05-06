class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev = self.first = self.last = None
        def trav(root):
            if root:
                trav(root.left)
                if self.prev !=None and root.val<self.prev.val:
                    if self.first ==None:
                        self.first = self.prev
                    self.last = root
                self.prev = root
                trav(root.right)          
        trav(root)
        self.first.val, self.last.val = self.last.val,self.first.val
