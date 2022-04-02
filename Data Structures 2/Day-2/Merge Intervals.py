class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=0
        length = len(intervals)
		
        while(i<length -1):
            if(intervals[i][1]>=intervals[i+1][0]):
                intervals[i][1]=max(intervals[i+1][1],intervals[i][1])
                intervals.pop(i+1)
                length-=1
            else:
                i+=1
				
        return intervals
