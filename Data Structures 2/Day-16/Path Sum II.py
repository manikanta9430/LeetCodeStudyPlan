class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        result = []
        # pass our result array in which is editted in place as we find
        # leafs that meet our criteria
        self.dfs(root, targetSum, [], result)
        return result
        
    def dfs(self, node, target, path, result):
        if not node: return
        
        target -= node.val
        
        # add node to the current path explored
        path.append(node.val)
        
        # if we're a leaf node, check we meet the criteria and add a copy
        # of the path to the result array. Adding a reference will mean
        # we end up with empty paths once all nodes have been explored
        if not node.left and not node.right and target == 0:
            result.append(path.copy())
            
        # explore left and right chilren if any
        self.dfs(node.left, target, path, result)
        self.dfs(node.right, target, path, result)
            
        # remove the node when we've finished exploring it's children
        # so it won't be in the path for parent nodes anymore
        path.pop()
