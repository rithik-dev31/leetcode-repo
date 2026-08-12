// Last updated: 8/12/2026, 11:31:02 AM
class Solution {
    public void rotate(int[] nums, int k) {
        
        int n=nums.length;
        int k1=k%n;

        reverse(nums,0,n-1);
        reverse(nums,0,k1-1);
        reverse(nums,k1,n-1);

    }

    public void reverse(int [] nums,int l,int r){
        while(l<r){
            int temp = nums[l];
            nums[l] = nums[r];
            nums[r] = temp;

            l+=1;
            r-=1;
        }

    }
}