class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        
		# prefix sum each row
        for row in matrix:
            for i in range(1, n):
                row[i] = row[i] + row[i-1]
            row.insert(0, 0)
        
        ans = -inf
        for i in range(n):
            for j in range(i, n):
                arr = [0] # init with a 0 in case cur_sum == k at a paricular row
                cur_sum = 0
                for r in range(m):
                    cur_sum += matrix[r][j+1] - matrix[r][i] # submatrix sum row 0 to r
                    x = bisect_left(arr, cur_sum - k) # search for the best candidate from earlier rows
                    if x < len(arr):
                        if arr[x] == cur_sum - k:
                            return k
                        else:
                            ans = max(ans, cur_sum - arr[x])
                    insort(arr, cur_sum) # update sorted list of cumulative sums
        
        return ans
