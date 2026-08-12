# Last updated: 8/12/2026, 11:26:53 AM
class Solution(object):
    def countValidPrefixes(self, s):
        """
        :type s: str
        :rtype: int
        """
        ze=0
        on=0
        an=0

        for ch in s:
            if ch=='0':
                ze+=1
            else:
                on+=1

            if abs(ze-on)<=1:
                an+=1

        return an