# Last updated: 8/12/2026, 11:27:15 AM
class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break

        values = set(nums)

        while prefix_sum in values:
            prefix_sum += 1

        return prefix_sum