class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        merge = []
        for idx, interval in enumerate(intervals):
            if interval[1] < newInterval[0]:
                merge.append(interval)
            if not (newInterval[1] < interval[0] or newInterval[0] > interval[1]):
                newInterval = [min(newInterval[0], interval[0]), 
                               max(newInterval[1], interval[1])]
            if newInterval[1] < interval[0]:
                merge.append(newInterval)
                return merge + intervals[idx:]
        # dont forget this step to add newInterval if the intervals is [], or merged to the end of list
        merge.append(newInterval)
        return merge
