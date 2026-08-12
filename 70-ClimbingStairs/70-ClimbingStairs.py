# Last updated: 8/12/2026, 11:32:39 AM
class Solution:

    
    def climbStairs(self, n: int) -> int:
        
        if n<=0:
            return n

        dp = [0] * (n + 1)

        if dp[n]!=0:
            return dp[n]
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        
        return dp[n]

