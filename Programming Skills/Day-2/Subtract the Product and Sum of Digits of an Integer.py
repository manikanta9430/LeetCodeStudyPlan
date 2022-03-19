class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n2=n
        p=1
        s=0
        while n:
            curr = n%10
            p *= curr
            s +=curr
            n =n//10
        return (p-s)
