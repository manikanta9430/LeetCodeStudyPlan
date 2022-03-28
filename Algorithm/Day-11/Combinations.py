class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ls = []
        for i in range(1, n + 1):
            ls.append(i)
                
        res = []
        self.dfs(ls, k, [], res)
        return res
        
    def dfs(self, ls, k, path, res):
        if len(path) == k:
            res.append(path[:])
            return 
        
        for i, item in enumerate(ls):
            path.append(item)
            self.dfs(ls[i + 1:], k, path, res)
            path.pop()
        return 
