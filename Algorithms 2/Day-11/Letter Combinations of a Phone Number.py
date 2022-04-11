class Solution:
    def letterCombinations(self, ds: str) -> List[str]:
        if not ds:
            return []
        
        ds = [int(d) for d in ds]
        _map = {2:'abc', 3:'def', 4:'ghi', 5:'jkl', 6:"mno",
                7:'pqrs', 8:'tuv', 9:'wxyz'}
        
        q = deque([[ch] for ch in _map[ds[0]]])
        for d in ds[1:]:
            nxt = _map[d]
            for _ in range(len(q)):
                l = q.popleft()
                for ch in nxt:
                    q.append(l+[ch])
        
        return [''.join(l) for l in q]
