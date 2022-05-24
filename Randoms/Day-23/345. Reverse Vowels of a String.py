class Solution:
    def reverseVowels(self, s: str) -> str:
        v=[]
        res=''
        for i in s:
            if i in 'aeiouAEIOU':
                v.append(i)
        for i in s:
            if i not in 'aeiouAEIOU':
                res+=i
            else:
                res+=v.pop()
        return res
