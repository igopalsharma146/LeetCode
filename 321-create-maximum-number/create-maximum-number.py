class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max(nums, length):
            stack = []
            remove = len(nums) - length

            for num in nums:
                while stack and remove and stack[-1] < num:
                    stack.pop()
                    remove -= 1
                stack.append(num)
            return stack[:length]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        answer = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a = get_max(nums1, i)
            b = get_max(nums2, k - i)
            candidate = merge(a[:], b[:])

            if candidate > answer:
                answer = candidate

        return answer