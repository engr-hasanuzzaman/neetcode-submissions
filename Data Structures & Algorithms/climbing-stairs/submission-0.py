class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * 46
        dp[0] = 1
        dp[1] = 1

        for n in range(2, n+1):
            dp[n] = dp[n-1] + dp[n-2]

        return dp[n] 




'''
4
1 1 1 1
1 2 1
1 1 2
2 1 1
2 2
'''
        