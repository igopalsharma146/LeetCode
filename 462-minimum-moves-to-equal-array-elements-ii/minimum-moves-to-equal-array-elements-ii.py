class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        midd=nums[mid]
        count=0
        for ch in nums:
            count += abs(midd-ch)
        return count