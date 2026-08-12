# Last updated: 8/12/2026, 11:32:03 AM
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mi=prices[0]
        max_profit = 0


        for price in prices:

            if price<mi:
                mi=price

            profit=price-mi  

            if profit>max_profit:
                max_profit=profit

        return max_profit
        