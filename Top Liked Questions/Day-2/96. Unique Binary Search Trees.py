class Solution(object):
    def numTrees(self, n):
        array = [0 for i in range(20)]
        array[0] = 1
        array[1] = 1
        for i in range(2,len(array)):
            for root in range(1,i+1):
                valLess = root - 1
                valMore = i - root
                array[i] += array[valLess] * array[valMore]
        return array[n]
