import queue 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        if not root:
            return res;
        
        que = queue.Queue()
        que.put(root)
        
        while not que.empty() :
            size = que.qsize()
            rec = []
            
            for i in range(size):
                cur = que.get()
                rec.append(cur.val)
                
                if cur.left:
                    que.put(cur.left)
                if cur.right:
                    que.put(cur.right)
            
            res.append(rec)
        
        return res
