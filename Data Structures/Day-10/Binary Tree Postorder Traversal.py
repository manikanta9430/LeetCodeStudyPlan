class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        if(root==None):
            return
        stack=[root]
        top=0
        while(stack):
            while(stack[top]==None):
                stack.pop()
                top-=1
            if(top-1>=0 and stack[top]==stack[top-1]):
                output.append(stack[top].val)
                stack.pop()
                stack.pop()
                top-=2
            else:
                stack.append(stack[top])
                stack.append(stack[top].right)
                stack.append(stack[top].left)
                top+=3
        return output 
