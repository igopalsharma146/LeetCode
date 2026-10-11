class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            if n % (i + 1) == 0:
                res += nums[i] * nums[i]
        return res


        # ans = 0
        # n = len(nums)
        # for i in range(1, n + 1):
        #     if n % i == 0:
        #         ans += nums[i - 1] * nums[i - 1]
        # return ans