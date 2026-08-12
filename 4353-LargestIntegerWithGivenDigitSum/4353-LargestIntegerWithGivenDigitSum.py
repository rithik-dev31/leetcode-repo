# Last updated: 8/12/2026, 11:26:55 AM
class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s>9*n:
            return -1

        if s==0:
            return 0

        ans=[]

        for i in range(n):
            d=min(9,s)
            ans.append(str(d))

            s-=d
        return int("".join(ans))