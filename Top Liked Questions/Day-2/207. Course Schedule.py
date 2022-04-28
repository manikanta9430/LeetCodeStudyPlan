class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = [set() for i in range(numCourses)]
        for p in prerequisites:
            courses[p[0]].add(p[1])
        visited = set()
        required = set()

        def tryFinish(i):
            for j in courses[i]:
                if j in required:
                    return -1
                if j not in visited:
                    required.add(j)
                    if tryFinish(j) == -1:
                        return -1
                    visited.add(j)
                    required.remove(j)
            visited.add(i)
        
        for i in range(numCourses):
            if i not in visited:
                if tryFinish(i) == -1:
                    return False
        return True
