class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        buffer = []   # (len(stack), count)
        n_lefts = 0  # state
        for p in s:
            if p == "(":
                n_lefts += 1
            else:
                if n_lefts:
                    n_lefts -= 1
                    total = 1
                    while len(buffer):
                        thresh, count = buffer.pop()
                        if thresh >= n_lefts:
                            total += count
                        else:
                            buffer.append((thresh,count))
                            break
                    buffer.append((n_lefts,total))
                    longest = max(longest, total)
                else:
                    buffer.clear()
                    n_lefts = 0
        if buffer:
            return max(longest, max(buffer,key=lambda x: x[1])[1])*2
        else:
            return longest*2

if __name__ == "__main__":
    solver = Solution()
    for test, sol in [("(()",2),(")()())",4),("",0),("()(()",2),
                      ("((()(((()))))",12)]:
        ans = solver.longestValidParentheses(test)
        assert sol == ans, f"Test '{test}': Expected {sol} but got {ans}."
        print(f"Passed '{test}'.")

