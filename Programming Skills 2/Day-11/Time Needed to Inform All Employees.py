class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subs = collections.defaultdict(list)
        for emp, man in enumerate(manager):
            subs[man].append(emp)
        
        q = collections.deque([(headID, informTime[headID])])
        totalMinutes = 0
        while q:
            sameLevelCounts = len(q)
            for _ in range(sameLevelCounts):
                curr, time = q.popleft()
                for sub in subs[curr]:
                    q.append((sub, time + informTime[sub]))
                    totalMinutes = max(totalMinutes, time + informTime[sub])
            
        return totalMinutes
