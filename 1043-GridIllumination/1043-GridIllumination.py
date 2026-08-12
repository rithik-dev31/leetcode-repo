# Last updated: 8/12/2026, 11:27:59 AM
from collections import Counter

class Solution:
    def gridIllumination(self, n: int, lamps: list[list[int]], queries: list[list[int]]) -> list[int]:
        rows = Counter()
        cols = Counter()
        diag = Counter()      # r - c
        anti = Counter()      # r + c

        lamp_set = set()

        # Turn on lamps
        for r, c in lamps:
            if (r, c) in lamp_set:
                continue
            lamp_set.add((r, c))
            rows[r] += 1
            cols[c] += 1
            diag[r - c] += 1
            anti[r + c] += 1

        ans = []

        directions = [
            (0, 0), (-1, -1), (-1, 0), (-1, 1),
            (0, -1), (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        for r, c in queries:
            # Check illumination
            if rows[r] > 0 or cols[c] > 0 or diag[r - c] > 0 or anti[r + c] > 0:
                ans.append(1)
            else:
                ans.append(0)

            # Turn off lamp in current cell and neighbors
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (nr, nc) in lamp_set:
                    lamp_set.remove((nr, nc))
                    rows[nr] -= 1
                    cols[nc] -= 1
                    diag[nr - nc] -= 1
                    anti[nr + nc] -= 1

        return ans