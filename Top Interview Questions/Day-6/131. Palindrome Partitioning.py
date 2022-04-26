class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = {}
        current = [] 
        res = [] 
        for i in range(len(s)):
            dp[(i,i)] = s[i]
         
        for diff in range(1, len(s)):
            for l in range(0, len(s)):
                r = l + diff
                if r > len(s)-1:
                    break
                if l == r: 
                    dp[(l,r)] = s[l]
                elif l + 1 == r and s[l] == s[r]: 
                    string = s[l] + s[r]
                    dp[(l,r)] =  string
                elif s[l] == s[r]:
                    if (l+1, r-1) in dp:
                        sub = dp[(l+1, r-1)]
                        string = s[l] + sub + s[r]
                        dp[(l,r)] = string
                        
        def backtracking(i):
            if i == len(s):
                res.append(current[::])
                return 
            
            for j in range(i, len(s)):
                if (i, j) in dp: 
                    current.append(dp[(i,j)])
                    backtracking(j + 1)
                    current.pop()
        
        backtracking(0)
        return res
