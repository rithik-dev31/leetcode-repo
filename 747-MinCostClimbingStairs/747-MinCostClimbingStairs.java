// Last updated: 8/12/2026, 11:28:42 AM
class Solution {
    public int minCostClimbingStairs(int[] cost) {
        if(cost.length==1){
            return cost[0];
        }

        int [] dp=new int[cost.length];
        int n=cost.length;
        
        dp[0]=cost[0];
        dp[1]=cost[1];
             

        for(int i=2;i<cost.length;i++){
            dp[i]=cost[i]+Math.min(dp[i-1],dp[i-2]);

        }

        return Math.min(dp[n-1],dp[n-2]);
    }
}