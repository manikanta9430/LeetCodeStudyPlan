class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:

        # Top-down dynamic programming
        # Time complexity: O(n^4), where n = len(s1) = len(s2)
        # Space complexity: O(n^3), where n = len(s1) = len(s2)
        @lru_cache(None)
        def topDownDP(s1_idx: int, s2_idx: int, length: int) -> bool:

            # Base case
            if length == 1:
                return s1[s1_idx] == s2[s2_idx]

            # There are two substrings with the same length:
            # sub1 = s1[s1_idx:s1_idx + length]
            # sub2 = s2[s2_idx:s2_idx + length]
            #
            # After scrambling substring sub1, it must match sub2. Approach:
            # Cut sub1 substring at each existing index and see if it is possible to get an exact match with sub2
            # whether we swap the slices or not
            for len1, len2 in zip(range(1, length), range(length - 1, 0, -1)):

                # Option #1 - don't swap sub1 slices
                if topDownDP(s1_idx, s2_idx, len1) and topDownDP(s1_idx + len1, s2_idx + len1, len2):
                    return True

                # Option #1 - swap sub1 slices
                if topDownDP(s1_idx, s2_idx + len2, len1) and topDownDP(s1_idx + len1, s2_idx, len2):
                    return True

            # Explored all options - not possible :(
            return False

        # Start DP
        return topDownDP(0, 0, len(s1))
