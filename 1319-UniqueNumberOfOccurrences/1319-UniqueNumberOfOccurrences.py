# Last updated: 8/12/2026, 11:27:46 AM
class Solution:
    def uniqueOccurrences(self, arr):
        freq = {}

        for num in arr:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        counts = freq.values()

        return len(counts) == len(set(counts))