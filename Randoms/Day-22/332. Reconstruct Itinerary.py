class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for u, v in tickets:
            heappush(graph[u], v) 

        def dfs(node):
            while graph[node]:
                nxt = heappop(graph[node])
                dfs(nxt)
            self.ans.append(node)
            
        self.ans = []
        dfs('JFK')
        return self.ans[::-1]
