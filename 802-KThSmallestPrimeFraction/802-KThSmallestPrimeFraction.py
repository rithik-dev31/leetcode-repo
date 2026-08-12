# Last updated: 8/12/2026, 11:28:38 AM
import heapq

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        heap = []

        # push smallest fraction from each numerator
        for i in range(n - 1):
            heapq.heappush(heap, (arr[i] / arr[-1], i, n - 1))

        # extract k-1 smallest
        for _ in range(k - 1):
            val, i, j = heapq.heappop(heap)

            if j - 1 > i:
                heapq.heappush(heap, (arr[i] / arr[j - 1], i, j - 1))

        _, i, j = heapq.heappop(heap)
        return [arr[i], arr[j]]