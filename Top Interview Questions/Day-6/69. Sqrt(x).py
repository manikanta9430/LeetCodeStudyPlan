class Solution:
    def mySqrt(self, x: int) -> int:
        if x ==1 :
            return 1
        l = 0
        r = x//2 
        while l <= r :
            mid = (l + r) // 2
            key = mid*mid
            if key == x :
                return mid
            elif key < x : 
                l = mid + 1
            else:
                r = mid - 1 
        return r
