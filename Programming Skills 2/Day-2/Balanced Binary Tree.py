class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def helper(self, root):
        if not root:
            return 0
        
        return max(self.helper(root.left), self.helper(root.right)) + 1
