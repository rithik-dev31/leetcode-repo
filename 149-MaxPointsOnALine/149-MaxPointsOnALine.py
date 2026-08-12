# Last updated: 8/12/2026, 11:31:49 AM
from collections import defaultdict
from math import gcd

class Solution(object):
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)

        best = 1

        for i in range(len(points)):
            slopes = defaultdict(int)

            for j in range(i + 1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    g = gcd(dx, dy)
                    dx //= g
                    dy //= g

                    if dx < 0:
                        dx = -dx
                        dy = -dy

                slopes[(dx, dy)] += 1

            current = 1
            for count in slopes.values():
                current = max(current, count + 1)

            best = max(best, current)

        return best