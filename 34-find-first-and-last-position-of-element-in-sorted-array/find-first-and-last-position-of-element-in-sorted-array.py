class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def lowerBound():
            left, right = 0, len(nums) - 1
            ans = len(nums)

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] >= target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans

        def upperBound():
            left, right = 0, len(nums) - 1
            ans = len(nums)

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    ans = mid
                    right = mid - 1
                else:
                    left = mid + 1

            return ans

        lb = lowerBound()

        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]

        ub = upperBound()

        return [lb, ub - 1]