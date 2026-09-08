class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        f1 = {}
        for num in nums:
            f1[num] = f1.get(num, 0) + 1

        for num in sorted(f1, reverse=True):
            k -= f1[num]
            if k <= 0:
                return num