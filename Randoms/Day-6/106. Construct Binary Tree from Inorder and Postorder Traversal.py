class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        def rec(ino,post,side):
            if not ino or not post:
                return None
            p = post.pop(-1)
            root = TreeNode(p)
            index = ino.index(p)
            root.right = rec(ino[index+1::],post,side+1)
            root.left = rec(ino[0:index],post,side)
            return root
        return rec(inorder,postorder,1)
