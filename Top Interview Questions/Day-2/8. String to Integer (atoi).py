class Solution:
    def myAtoi(self, s: str) -> int:
        sign=1
        num=0
        switch={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        s=s.strip()
        for i,c in enumerate(s):
            nxt= i+1 if i+1<len(s) else len(s)-1
            if c=="+":
                sign=1
                if s[nxt] not in '0123456789':
                    return 0
            elif c=="-":
                sign=-1
                if s[nxt] not in '0123456789':
                    return 0
            elif c not in '0123456789':
                return 0
            elif c in '0123456789':
                num=num*10+switch[c]
                if s[nxt] not in '0123456789':
                    break
        num=num*sign
        if num>2**31-1:
            num=2**31-1
        if num<-2**31:
            num=-2**31
        return num
