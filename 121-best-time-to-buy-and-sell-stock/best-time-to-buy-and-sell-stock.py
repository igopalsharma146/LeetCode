class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        mini=float('inf')
        for ch in prices:
            mini=min(mini,ch)
            max_profit=max(max_profit,ch - mini)
        return max_profit
            