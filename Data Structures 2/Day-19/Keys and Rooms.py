class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = {}
        queue = [0]
        while queue:
            s = queue.pop(0)
            visited[s] = True
            for key in rooms[s]:
                if key not in visited:
                    queue.append(key)
                
        return len(visited) == len(rooms)
