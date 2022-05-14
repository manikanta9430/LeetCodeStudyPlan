class Solution:
    def traverse(self,node,cur):
        if node:
            cur = chr(node.val + 97) + cur
            if not node.left and not node.right:
                
                if self.ans == None or cur < self.ans : self.ans = cur
            cpy = cur
            self.traverse(node.left,cur)
            self.traverse(node.right,cpy)
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.ans = None
        self.traverse(root,"")
        return self.ans
