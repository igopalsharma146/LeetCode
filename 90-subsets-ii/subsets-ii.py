class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def backtrack(index, subset):
            res.append(subset[:])
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        backtrack(0, [])
        return res