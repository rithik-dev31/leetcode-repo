# Last updated: 8/12/2026, 11:26:57 AM
class Solution(object):
    def countRatioSubarrays(self, nums, a, b):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :rtype: int
        """
        n=len(nums)

        r=0

        for i in range(n):
            e=0
            o=0

            for j in range(i,n):
                if nums[j]%2==0:
                    e+=1
                else:
                    o+=1

                if o>0 and e*b<=o*a:
                    r+=1

        return r