class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia = 0
        self.dfs(root)
        return self.dia
    #bottom up dfs
    def dfs(self, node):
        #1.base case
        if not node:
            return 0
        #2.do recursive left and right
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        #3.construct the answer
        self.dia = max(self.dia, left+right)

        #4. do the recursice for step 2
        return 1+max(left, right)
