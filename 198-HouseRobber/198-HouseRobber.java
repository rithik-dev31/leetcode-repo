// Last updated: 8/12/2026, 11:30:58 AM
class Solution {

    
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }

        int []df=new int[nums.length];

        df[0]=nums[0];
        df[1]=Math.max(df[0],nums[1]);


        for (int i=2;i<nums.length;i++){
            df[i]=Math.max(df[i-1],nums[i]+df[i-2]);
        }

        return df[nums.length-1];

    }
}