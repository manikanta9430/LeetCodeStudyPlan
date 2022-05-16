from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # ct[i] = number papers with i-citations, this array will be later
        # modified to represent number of papers with at-least i-citations
        ct = [0] * (1 + max(citations))

        for e in citations:
            ct[e] += 1

        for h_idx in reversed(range(1, len(ct))):
            if ct[h_idx] >= h_idx:
                return h_idx

            # number of papers with at least h_idx - citations =
            # (number of papers with h_idx - 1) + (number of papers with more than h_idx - 1)
            ct[h_idx - 1] += ct[h_idx]

        return 0
