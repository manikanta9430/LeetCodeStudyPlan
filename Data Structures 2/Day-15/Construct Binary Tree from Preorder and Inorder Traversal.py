class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        Hash = {num:i for i,num in enumerate(inorder)}
        def helper(i_left,i_right):
            if i_left > i_right:
                return None
            val = preorder.pop(0)
            root = TreeNode(val)
            Index = Hash[val]
            
            root.left = helper(i_left,Index-1)
            root.right = helper(Index+1,i_right)
            return root
        return helper(0,len(preorder)-1)
