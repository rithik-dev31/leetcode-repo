# Last updated: 8/12/2026, 11:28:19 AM
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left], nums[right] = nums[right], nums[left]

            if nums[left] % 2 == 0:
                left += 1

            if nums[right] % 2 == 1:
                right -= 1

        return nums