class Solution:
    def findPathSum(self,root,path,targetSum):
        if root is None:
            return
        path.append(root.val)
        self.findPathSum(root.left,path,targetSum)
        self.findPathSum(root.right,path,targetSum)
       #for loop for finding the targetSum
        f = 0
        for i in range(len(path)-1,-1,-1):
            f += path[i]
            if f == targetSum:
                self.totalPath += 1
                
        path.pop()
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
	#path variable to store the number of times targetSum is occur
        self.totalPath = 0
	#path stack array to store the element while traversing
        path = []
        self.findPathSum(root,path,targetSum)
        return self.totalPath
