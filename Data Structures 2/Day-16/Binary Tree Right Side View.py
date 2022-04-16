class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        res=[]
        q=deque()
        q.append(root)
        
        while q:
            res.append(q[-1].val)
			length=len(q)
            for i in range(length):
                node=q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
        return res
