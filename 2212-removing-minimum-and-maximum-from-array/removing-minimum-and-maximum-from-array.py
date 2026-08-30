class Solution(object):
    def minimumDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxi = float("-inf")
        mini = float("inf")
        maxi_ind = 0
        mini_ind = 0

        for i in range(n):
            if nums[i] > maxi:
                maxi = nums[i]
                maxi_ind = i

            if nums[i] < mini:
                mini = nums[i]
                mini_ind = i

        left = max(maxi_ind, mini_ind) + 1
        right = n - min(maxi_ind, mini_ind)
        mixed = min(maxi_ind, mini_ind) + 1 + n - max(maxi_ind, mini_ind)
        return min(left, right, mixed)
        