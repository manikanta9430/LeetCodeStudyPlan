class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res=[]
        d={}
        for k in words:
            d[k]=d.get(k,0)+1
        
        skip=len(words[0])
        i=0
        while i<len(s):
            h=d.copy()
            j=i
            m=i
            t=len(words)
            while j<len(s) and t>0:
                j+=skip
                if s[m:j] in h and h[s[m:j]]>0:
                    h[s[m:j]]-=1
                    t-=1
                    m=j
                else:break
            if t==0:
                res.append(i)
            i+=1
        
        return res
