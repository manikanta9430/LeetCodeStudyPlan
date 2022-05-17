class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        open, close = self.getMinRemoval(s)
        res = set()

        self.dfs(s, open, close, {}, res)
        return res

    def dfs(self, s, open, close, hmap, res):
        if s in hmap:
            return
        if open == close == 0:
            hmap[s] = True
            if self.getMinRemoval(s) == (0, 0):
                res.add(s)
            return

        for j in range(len(s)):
            if s[j] == '(' and open != 0:
                newS = s[:j] + s[j+1:]
                self.dfs(newS, open-1, close, hmap, res)
                hmap[newS] = True
            elif s[j] == ')' and close != 0:
                newS = s[:j] + s[j+1:]
                self.dfs(newS, open, close-1, hmap, res)
                hmap[newS] = True

    def getMinRemoval(self, s):
        stack = []
        for c in s:
            if c not in '()':
                continue

            if c == '(':
                stack.append(c)
            elif stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(c)
        l = r = 0
        for c in stack:
            if c == '(':
                l += 1
            else:
                r += 1
        return l, r
