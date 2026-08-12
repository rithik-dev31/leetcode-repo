# Last updated: 8/12/2026, 11:26:52 AM
class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum=0
        SquareSum=0

        for digit in str(n):
            d=int(digit)
            digitSum+=d
            SquareSum+=d*d

        return SquareSum-digitSum>=50