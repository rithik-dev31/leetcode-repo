# Last updated: 8/12/2026, 11:28:47 AM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        l=len(cost)

        dp=[0]*(l+1)

        dp[0]=cost[0]
        dp[1]=cost[1]

        for i in range(2,len(cost)):
            dp[i]=cost[i]+min(dp[i-1],dp[i-2])

        return min(dp[l-1],dp[l-2])
        