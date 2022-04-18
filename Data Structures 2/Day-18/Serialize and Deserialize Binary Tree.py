class Codec:

    def serialize(self, root):
        if not root:
            return ""
        string=""
        string+=str(root.val)+","
        q=deque()
        q.append(root)
        
        while q:
            for i in range(len(q)):
                node=q.popleft()
                if node.left:
                    string+=str(node.left.val)+","
                    q.append(node.left)
                else:
                    string+="#,"
                if node.right:
                    string+=str(node.right.val)+","
                    q.append(node.right)
                else:
                    string+="#,"
        
        return string
        
        
        
    def deserialize(self, data):
        if not data:
            return None
        
        stack=data[:-1].split(",")
        
        q=deque()
        root=TreeNode(int(stack.pop(0)))
        q.append(root)
        
        while q:
            node=q.popleft()
            
            temp1=stack.pop(0)
            if temp1=="#":
                node.left=None
            else:
                node.left=TreeNode(int(temp1))
                q.append(node.left)
            
            temp2=stack.pop(0)
            if temp2=="#":
                node.right=None
            else:
                node.right=TreeNode(int(temp2))
                q.append(node.right)
                
        return root
