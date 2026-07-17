class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # brute force
        # for i in range(1, len(nums)+1):
        #     if i not in nums:
        #         return i

        # return len(nums)+1
        
        # # better
        # s = set(nums)
        # for i in range(1, len(nums)+1):
        #     if i not in s:
        #         return i

        # return len(nums)+1


        # optimal
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i] - 1

            if 1 <= nums[i] <= n and nums[i] != nums[correct]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1