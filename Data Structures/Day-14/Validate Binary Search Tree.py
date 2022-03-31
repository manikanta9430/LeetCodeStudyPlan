class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        UP_LIMIT = 2 **32
        LOW_LIMIT = -(2 ** 31) - 1
        return self.validSub(root, UP_LIMIT, LOW_LIMIT)
        
    def validSub(self, root, up, low):
        left = root.left
        right = root.right
        if left:
            if left.val >= root.val or left.val <= low:
                return False
            if not self.validSub(left, root.val, low):
                return False
        if right:
            if right.val <= root.val or right.val >= up:
                return False
            if not self.validSub(right, up, root.val):
                return False
        return True
