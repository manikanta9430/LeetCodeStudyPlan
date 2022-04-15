class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        ans = []
        queue = []
        
        queue.append(root)
        flag =True
        res = []
        while queue:
            
            count = len(queue)
            for i in range(count):
                x = queue.pop(0)
                if flag:
                    res.append(x.val)
                else:
                    res.insert(0,x.val)
                if x.left is not None:
                    queue.append(x.left)
                if x.right is not None:
                    queue.append(x.right)
            flag= not flag
            ans.append(res)
            res = []
            
        return ans
