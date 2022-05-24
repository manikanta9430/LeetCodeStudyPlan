MAX_VAL = 10 ** 4

class OrderedDisjoinSet:
    def __init__(self, size):
        self.size = size
        self.parents = list(range(size))
        
    def find(self, x):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])  # Path compression
        return self.parents[x]
    
    def is_joined(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        return roota == rootb
    
    def join(self, a, b):
        roota = self.find(a)
        rootb = self.find(b)
        
        if roota == rootb:
            return False
        
        if rootb < roota:  # Alway join to smallest number
            a, b = b, a
            roota, rootb = rootb, roota
            
        self.parents[rootb] = roota            
        return True
    
class SummaryRanges:
    def __init__(self):
        self.ranges = {}  # {start: end}
        self.djs = OrderedDisjoinSet(MAX_VAL + 1)
        self.seen = set()
        

    def addNum(self, val: int) -> None:
	   # Union find to add val - 1, val +1 to merge range. ~O(1)
        ranges = self.ranges
        djs = self.djs
        seen = self.seen
        if val in seen:
            return
        ranges[val] = val
        seen.add(val)
        for neighbor in (val-1, val+1):
            if neighbor >= 0 and neighbor in seen:
                prefmax = ranges.get(neighbor, -1)
                djs.join(val, neighbor)
                ranges.pop(val, None)
                ranges.pop(neighbor, None)
                ranges[min(val, djs.find(val))] = max(val, prefmax)           

    def getIntervals(self) -> List[List[int]]:
        # return sorted(self.ranges.items())   # O(nlogn) in worse case where there is no merged range yet ie each range is it own number pair [i, i]> This is faster for sure
		ranges = self.ranges
		i = 0
		output = []
		while i <= MAX_VAL:  # O(MAX_VAL) ~ O(1) :))
			if i in ranges:
				output.append(i, ranges[i])
				i = ranges[i] + 1
			else:
				i += 1
		return output
