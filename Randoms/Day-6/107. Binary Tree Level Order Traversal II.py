class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return
        else:
            
            queue = [root]
            ans = []
            
            while queue:
                
                len_q = len(queue)
                level_nodes = []
                
                for _ in range(len_q):
                    root = queue.pop(0)
                    level_nodes.append(root.val)
                    
                    if root.left:
                        queue.append(root.left) 
                    if root.right:
                        queue.append(root.right)
                        
                ans.append(level_nodes)
            return ans[::-1]
