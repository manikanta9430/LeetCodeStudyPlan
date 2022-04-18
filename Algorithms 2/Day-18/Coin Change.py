from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        visited = set()
        visited.add(0)
        
        q = deque()
        q.append(0)
        
        curr_coin_count = 0
        
        while q: 
            curr_coin_count += 1
            for _ in range(len(q)):
                curr_amount = q.popleft()
                for coin in coins:
                    next_amount = curr_amount + coin

                    if next_amount == amount:
                        return curr_coin_count

                    if next_amount < amount and next_amount not in visited:
                        q.append(next_amount)
                        visited.add(next_amount)
                    
        return -1
