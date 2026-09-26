class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
        
        return dp[amount] if dp[amount] != float('inf') else -1

        
        # if amount < 0:
        #     return -1
        # if amount == 0:
        #     return 0
        
        # min_count = float('inf')
        
        # for coin in coins:
        #     res = self.coinChange(coins, amount - coin)
        #     if res != -1:
        #         min_count = min(min_count, 1 + res)
                
        # return min_count if min_count != float('inf') else -1