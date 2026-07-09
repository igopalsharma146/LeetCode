class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        result=[]
        result = set()

        for i in range(n):
            for j in range(i + 1, n):
                seen = set()

                for k in range(j + 1, n):
                    fourth = target - (nums[i] + nums[j] + nums[k])

                    if fourth in seen:
                        temp = tuple(sorted([nums[i], nums[j], nums[k], fourth]))
                        result.add(temp)

                    seen.add(nums[k])
        return list(result)
                    