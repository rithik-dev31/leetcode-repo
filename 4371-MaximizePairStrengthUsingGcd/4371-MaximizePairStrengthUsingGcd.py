# Last updated: 8/12/2026, 11:26:59 AM
from fractions import gcd

class Solution(object):
    def maxPairStrength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        a=0
        n=len(nums)

        for i in range(n):
            for j in range(i+1):
                g=gcd(nums[i],nums[j])
                a=max(a,(nums[i]*nums[j])//(g*g))

        return a
        