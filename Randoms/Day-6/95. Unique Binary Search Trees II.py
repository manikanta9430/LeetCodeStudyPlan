class Solution:
    """
    I can think of recursive approach
    """
    def fun(self, nodes):   
        ans = []
        if len(nodes) == 0:
            return [None]
        
        if len(nodes) == 1:
            return [TreeNode(nodes[0])]
        
        for i in range(len(nodes)):
            left_subtrees = self.fun(nodes[:i])
            right_subtrees = self.fun(nodes[i+1:])
            for ltree in left_subtrees:
                for rtree in right_subtrees:
                    root = TreeNode(nodes[i])
                    root.left = ltree
                    root.right = rtree
                    ans.append(root)
        return ans
        
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nodes = [i for i in range(1, n+1)]
        return self.fun(nodes)
