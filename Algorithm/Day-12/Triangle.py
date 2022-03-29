class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        def dfs(triangle,layer,ind,dic):
            
            if layer == n:
                return 0
            
            if (layer,ind) in dic:
                return dic[(layer,ind)]
            
            dic[(layer,ind)] = min(triangle[layer][ind] + dfs(triangle,layer+1,ind,dic),triangle[layer][ind] + dfs(triangle,layer+1,ind+1,dic))
            return dic[(layer,ind)]
        
        return dfs(triangle,0,0,{})
