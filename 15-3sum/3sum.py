class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()

        for i in range(0,len(nums)):
            seen = set()

            for j in range(i + 1, len(nums)):
                third = -(nums[i] + nums[j])

                if third in seen:
                    temp = tuple(sorted([nums[i], nums[j], third]))
                    result.add(temp)

                seen.add(nums[j])
        return list(result)
