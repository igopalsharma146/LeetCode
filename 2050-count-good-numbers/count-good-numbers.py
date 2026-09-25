class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7

        evenPosition = (n + 1) // 2
        oddPosition = n // 2

        evenWays = pow(5, evenPosition, MOD)
        oddWays = pow(4, oddPosition, MOD)

        return (evenWays * oddWays) % MOD