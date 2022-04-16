class Solution:
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [(1, 1) for _ in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[i] > nums[j]:
                    if dp[j][0] + 1 > dp[i][0]:
                        dp[i] = (1+dp[j][0], dp[j][1])
                    elif dp[j][0] + 1 == dp[i][0]:
                        dp[i] = (dp[i][0], dp[i][1]+dp[j][1])
        #print(dp)
        ans = -1
        max_val = -1
        for elem in dp:
            if elem[0] == max_val:
                ans+=elem[1]
                
            elif elem[0] > max_val:
                max_val = elem[0]
                ans = elem[1]
        return ans
