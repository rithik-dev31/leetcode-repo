# Last updated: 8/12/2026, 11:31:32 AM
class Solution(object):
    def titleToNumber(self, columnTitle):
        answer = 0

        for ch in columnTitle:
            answer = answer * 26 + (ord(ch) - ord('A') + 1)

        return answer