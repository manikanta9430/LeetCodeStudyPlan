class Solution:
    def minWindow(self, s: str, t: str) -> str:      
        cnt = collections.defaultdict(int)
        for x in t:
            cnt[x] -=1
        
        pt = 0
        minl = sys.maxsize
        res = 0
        
        for i in range(len(s)):
            cnt[s[i]] += 1
            while min(cnt.values()) >= 0:
                if i-pt + 1 < minl:
                    res = (pt, i+1)
                    minl = i-pt + 1
                cnt[s[pt]] -= 1
                pt += 1
                
        if not res:
            return ''
        
        return s[res[0]:res[1]]

