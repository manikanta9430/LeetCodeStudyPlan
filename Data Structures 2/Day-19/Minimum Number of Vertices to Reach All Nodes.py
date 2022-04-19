class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        from_set = set()
        to_set = set()
        for f, t in edges:
            from_set.add(f)
            to_set.add(t)
        return list(from_set - to_set)
