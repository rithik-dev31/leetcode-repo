# Last updated: 8/12/2026, 11:31:54 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total=0
        for i in nums:
            total^=i
        return total