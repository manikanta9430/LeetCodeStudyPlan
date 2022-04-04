class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        low,high = 0,1
        count = 0
        while high < len(intervals):
            if intervals[high][0] < intervals[low][1]:
                if intervals[high][1] > intervals[low][1]:
                    high +=1
                else:
                    low = high
                    high += 1
                count += 1
            else:
                low = high
                high += 1
        return count
