# Last updated: 8/12/2026, 11:29:32 AM
class Solution(object):
    def addDigits(self, num):
        if num == 0:
            return 0

        if num % 9 == 0:
            return 9

        return num % 9