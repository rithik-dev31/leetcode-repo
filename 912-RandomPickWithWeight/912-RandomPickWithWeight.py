# Last updated: 8/12/2026, 11:28:26 AM
from itertools import accumulate
from bisect import bisect_left
import random

class Solution:

    def __init__(self, w: List[int]):
        self.prefix = list(accumulate(w))
        self.total = self.prefix[-1]

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        return bisect_left(self.prefix, target)