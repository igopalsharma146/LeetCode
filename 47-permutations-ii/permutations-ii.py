class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        used = [False] * len(nums)

        def solve(subset):
            if len(subset) == len(nums):
                if subset not in res:
                    res.append(subset[:])
                return

            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                subset.append(nums[i])

                solve(subset)

                subset.pop()
                used[i] = False

        solve([])
        return res