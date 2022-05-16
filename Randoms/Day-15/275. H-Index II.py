class Solution(object):
    def hIndex(self, citations):
        start,end = len(citations)-1, len(citations)-1
        
        while citations:
            if citations[-1] > 0 and citations[-1] >= (end-start+1): #peek the tail and see if the height is still not smaller than the width
                citations.pop()
                start -= 1
            else:
                return end - start
        return end - start
