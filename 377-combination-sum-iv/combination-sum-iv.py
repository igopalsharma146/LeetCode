class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        return dp[target]


        # MEMORY LIMIT EXCEED
        # res = []
        # def comb(sum1, subset):
        #     if sum1 == target:
        #         res.append(subset[:])
        #         return

        #     if sum1 > target:
        #         return

        #     for num in nums:
        #         subset.append(num)
        #         comb(sum1 + num, subset)
        #         subset.pop()
        # comb(0, [])
        # return len(res)