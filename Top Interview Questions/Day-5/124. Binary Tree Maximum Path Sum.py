class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_tree = defaultdict(lambda:[-float('inf'), -float('inf')]) #max_tree[treenode] = (max from left, max from right)
        max_return = -float('inf')
        
        def traverse(node):
            nonlocal max_return
            if node.left:
                max_tree[node][0] = max(max(traverse(node.left)) + node.val, node.val)
            else:
                max_tree[node][0] = node.val
            if node.right:
                max_tree[node][1] = max(max(traverse(node.right)) + node.val, node.val)
            else:
                max_tree[node][1] = node.val
            max_return = max(max_return, node.val, sum(max_tree[node]) - node.val, max(max_tree[node]))    
            return max_tree[node]
        traverse(root)
        return max_return
