# Last updated: 8/12/2026, 11:32:26 AM
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        for j in range(len(nums)):
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    temp=nums[i]
                    nums[i]=nums[i+1]
                    nums[i+1]=temp
              