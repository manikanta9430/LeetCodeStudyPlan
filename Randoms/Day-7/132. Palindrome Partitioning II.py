class Solution:
    def minCut(self, s: str) -> int:
        def isPal(s, st, end):
            if end - st <= 1:
                return True
            if s[st] != s[end-1]:
                return False
            return isPal(s, st+1, end-1)
        @cache
        def getCut(s, st=0):
            #print(f'{s[st:]=}')
            l = len(s)
            if st >= l-1:
                return l - st - 1
            pals = [i+1 for i in range(st, l) if isPal(s, st, i+1)]
            #print(f'{st=} {pals=}')
            # check from long to short
            minCut = math.inf
            for end in reversed(pals):
                cut = getCut(s, end) + 1
                if cut <= 1:
                    return cut
                minCut = min(minCut, cut)
            return minCut
        return getCut(s)
