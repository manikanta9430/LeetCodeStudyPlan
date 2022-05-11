from sortedcontainers import SortedList
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
    
        # to store heights seen so far at a given pt
        heights = SortedList()
        
        bs = []    
        for s, e, h in buildings:
            bs.append([s, h]) # to increase at building start pt
            bs.append([e, -h]) # to decrease at builing end pt
        # sort pts by negative of heights that it will skip decreasing pt where
        # pt1 = [x, h] and pt2 = [x, -h], two pts at the same location
        bs.sort(key=lambda x: (x[0], -x[1]))
        
        ans = [[-1, -1]]
        
        for pt, h in bs:
            pre_pt, pre_h = ans[-1]
            
            if h < 0:
                heights.discard(-h)                
                if not heights:
                    ans.append([pt, 0])                
                elif -h == pre_h and not -h == heights[-1]:
                    ans.append([pt, heights[-1]]) 
            else:
                heights.add(h)
                if h > pre_h:
                    ans.append([pt, h])
                    
        return ans[1:]
