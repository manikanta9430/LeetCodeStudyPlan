class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        
        def getIntersection(fl, sl):
            maxStartTime = max(fl[0], sl[0])
            minEndTime = min(fl[1], sl[1])
            
            if maxStartTime <= minEndTime:
                result.append([maxStartTime, minEndTime])
            return
            
        
        while len(firstList)!=0 and len(secondList)!=0:
            getIntersection(firstList[0], secondList[0])
            
            # greedily pop the item that ends first
            if firstList[0][1] < secondList[0][1]:
                firstList.pop(0)
            else:
                secondList.pop(0)
        
        return result
