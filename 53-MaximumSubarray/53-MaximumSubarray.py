# Last updated: 8/12/2026, 11:32:42 AM
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current=nums[0]
        max_sum=nums[0]

        for i in range(1,len(nums)):
            
            current=max(current+nums[i],nums[i])
            max_sum=max(max_sum,current)

        return max_sum        