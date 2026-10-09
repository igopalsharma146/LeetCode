class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0

        nums.sort()
        count = 0
        left, right = 0, 1
        n = len(nums)
        while right < n:
            if left == right:
                right += 1
                continue

            diff = nums[right] - nums[left]

            if diff == k:
                count += 1
                left_val = nums[left]
                right_val = nums[right]
                while left < n and nums[left] == left_val:
                    left += 1

                while right < n and nums[right] == right_val:
                    right += 1

            elif diff < k:
                right += 1
            else:
                left += 1
        return count