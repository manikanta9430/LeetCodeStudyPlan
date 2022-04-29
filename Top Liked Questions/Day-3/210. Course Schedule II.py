class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=[[] for _ in range(numCourses)]   #build adjacent list
        for pair in prerequisites:
            graph[pair[1]].append(pair[0])
        
        visited=[0]*numCourses   #mark the status of the nodes
													#not visited yet(0), being visited(-1), already visited(1)
        order=[]   #post-order traversal result
		
        def dfs(node):
            if visited[node]==0:
                visited[node]=-1
                for n in graph[node]:
                    if not dfs(n):
                        return False     
                visited[node]=1
                order.append(node)
                return True
            if visited[node]==1:
                return True
            if visited[node]==-1:      #a cycle is detected
                return False
        for node in range(numCourses):
            if not dfs(node):
                return []     # A cycle exists
        
        return reversed(order)
