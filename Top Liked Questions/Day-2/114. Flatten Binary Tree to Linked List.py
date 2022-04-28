class Solution:
    def get_preorder_traversal(self, root, stack):
        if root is None:
            return
        stack.append(root)
        self.get_preorder_traversal(root.left, stack)
        self.get_preorder_traversal(root.right, stack)
        
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root is None:
            return
        
        stack = []
        self.get_preorder_traversal(root, stack)
        curr = stack[0]
        for node in stack[1:]:
            curr.right = node
            curr.left = None
            curr = node
