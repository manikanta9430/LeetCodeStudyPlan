class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res = list()
        if not root : return res

        s = list()
        cur = root
        while cur or s :
            if cur : 
                s.append(cur)
                cur = cur.left
            else :
                node = s[-1]
                s.pop()
                res.append(node.val)
                cur = node.right

        return res
