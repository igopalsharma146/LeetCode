class Solution(object):
    def maxWidthRamp(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # TLE Error
        # maxi=0
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]<=nums[j]:
        #             maxi=max(maxi,j-i)
        # return maxi

        maxi = 0
        n = len(nums)
        vp = [(nums[i], i) for i in range(n)]

        # Sort the list based on the element values
        vp.sort()

        min_index = vp[0][1]

        for i in range(1, n):
            current_index = vp[i][1]
            maxi = max(maxi, current_index - min_index)
            min_index = min(min_index, current_index)

        return maxi