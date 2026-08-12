// Last updated: 8/12/2026, 11:32:34 AM
class Solution {
    static int[] dp = new int[100];
    
    public int climbStairs(int n) {
        if(dp[0]!=1){
            dp[0]=1;
            dp[1]=1;
        }
        if(n<=1){
            return n;
        }

        if(dp[n]!=0){
            return dp[n];
        }
        
        for(int i=2;i<=n;i++){
            dp[i]=dp[i-1]+dp[i-2];
        }

        return dp[n];
    }
}