class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        result = []
        result.append(root.val)
        if root.left != None:
            result += self.preorderTraversal(root.left)
        if root.right != None:
            result += self.preorderTraversal(root.right)
        return result
