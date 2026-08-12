# Last updated: 8/12/2026, 11:27:14 AM
class Solution:
    def maxFrequencyElements(self, nums):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        max_freq = max(freq.values())

        result = 0

        for count in freq.values():
            if count == max_freq:
                result += count

        return result