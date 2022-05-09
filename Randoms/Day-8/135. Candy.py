class Solution(object):
    def candy(self, ratings):
        prev, ret, run = 1, 1, 0
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                if run != 0: prev = 1
                prev, ret, run = prev + 1, prev + ret + 1, 0
            else:
                run += 1
                if run == prev: run += 1
                if ratings[i] == ratings[i-1]: run, prev = 1, 1
                ret += run
        return ret
