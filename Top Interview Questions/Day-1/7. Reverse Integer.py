class Solution(object):
    def reverse(self, x):
        s=str(x)
        new=""
        if s[0]=="+" or s[0]=="-":  
            new+=s[0]
            s=s[1:]
        for i in range(len(s)-1,-1,-1):
            new+=s[i]
        new = int(new)
        if -2**31>new or new>((2**31)-1):
            return 0
        return new
