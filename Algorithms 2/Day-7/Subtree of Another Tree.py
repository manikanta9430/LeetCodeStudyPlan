class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        Q = []
        Q.append(root)
        possiblenodes = []
        while len(Q) > 0 :
            node = Q.pop(0)
            if node.val == subRoot.val:
                possiblenodes.append(node)
            
            
            if node.left is not None:
                Q.append(node.left)

            if node.right is not None:
                Q.append(node.right)

        for node in possiblenodes:
            if Solution.EqualTrees(node, subRoot):
                return True
        return False


    def EqualTrees(node1, node2):
        if node1 is None and node2 is not None:
            return False
        elif node1 is not None and node2 is None:
            return False
        elif node1 is not None and node2 is not None:
            if node1.val == node2.val:
                return Solution.EqualTrees(node1.left, node2.left ) and Solution.EqualTrees(node1.right, node2.right)
            else:
                return False
        else:
            return True
