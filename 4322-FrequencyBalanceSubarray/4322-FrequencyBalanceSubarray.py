# Last updated: 8/12/2026, 11:27:09 AM
from collections import defaultdict
from typing import List

class Solution:
    def getLength(self, nums: List[int]) -> int:
        dremovical = nums

        n = len(nums)
        ans = 1

        for i in range(n):
            freq = defaultdict(int)

            countFreq = defaultdict(int)

            mx = 0

            for j in range(i, n):
                x = nums[j]

                old = freq[x]

                if old:
                    countFreq[old] -= 1
                    if countFreq[old] == 0:
                        del countFreq[old]

                freq[x] += 1
                new = freq[x]

                countFreq[new] += 1
                mx = max(mx, new)

                length = j - i + 1

                # only one distinct value
                if len(freq) == 1:
                    ans = max(ans, length)
                    continue

                # mx must be even
                if mx % 2:
                    continue

                half = mx // 2

                # frequencies must be exactly {mx, half}
                if set(countFreq.keys()) != {mx, half}:
                    continue

                if countFreq[mx] == 0:
                    continue

                if countFreq[half] == 0:
                    continue

                ans = max(ans, length)

        return ans