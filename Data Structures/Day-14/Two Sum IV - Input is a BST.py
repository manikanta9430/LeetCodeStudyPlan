class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def orderBST(node):
            if node.left == None and node.right == None:
                return [node.val]
            out = []
            if node.left != None:
                out += orderBST(node.left)
            out.append(node.val)
            if node.right != None:
                out += orderBST(node.right)
            return out
        h = orderBST(root)
        
        for i in range(len(h)-1):
            num = k - h[i]
            if num in h[i+1:]:
                return True
        return False
