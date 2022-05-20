from sortedcontainers import SortedList
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre = self.get_prefix(nums)
        l = SortedList()
        ans = 0
        for i in range(1, len(pre)):
            l.add(pre[i - 1])
            u = pre[i] - lower
            d = pre[i] - upper
            ans += l.bisect_right(u) - l.bisect_left(d)
        return ans
    
    def get_prefix(self, nums):
        ans = [0]
        for num in nums:
            ans.append(ans[-1] + num)
        return ans
