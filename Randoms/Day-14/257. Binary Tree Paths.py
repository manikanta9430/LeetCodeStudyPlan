class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        stack = []
        TreeWalkUtil(root,stack,res)
        return res
        
def TreeWalkUtil( root, stack, res):
# push the current node in the stack
    stack.append(root.val)
# Recurse down left and then right node after checking if they exists
    if root.left:
        TreeWalkUtil(root.left,stack,res)
    if root.right:
        TreeWalkUtil(root.right,stack,res)
# If I'm at a node that has no children take the elements in stack and create a path
    if not root.left and not root.right:
        path = "->".join([str(node) for node in stack])
        res.append(path)
# Take the last elm out of stack since we are done at that level
    stack.pop()
