# Last updated: 8/12/2026, 11:29:23 AM
class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1