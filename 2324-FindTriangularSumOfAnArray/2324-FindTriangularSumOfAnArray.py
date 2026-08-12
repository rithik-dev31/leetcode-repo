# Last updated: 8/12/2026, 11:27:19 AM
class Solution(object):
        def triangularSum(self, nums):

            result = [nums]

            for i in range(len(nums) - 1):
                temp = result[-1]
                temp_res = []

                for j in range(len(temp) - 1):
                    temp_res.append((temp[j] + temp[j + 1]) % 10)

                result.append(temp_res)

            return result[-1][0]