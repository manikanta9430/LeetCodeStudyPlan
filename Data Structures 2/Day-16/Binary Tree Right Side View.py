class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        res=[]
        q=[]
        q.append(root)
        while(len(q)!=0):
            n=len(q)
            for i in range(n):
                curr=q.pop(0)
                ans=curr.val
                if curr.left!=None:
                    q.append(curr.left)
                if curr.right!=None:
                    q.append(curr.right)
            res.append(ans)
        return res
