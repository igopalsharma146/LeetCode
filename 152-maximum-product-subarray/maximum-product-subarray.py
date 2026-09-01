class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        max_prod = float('-inf')
        pref = suff = 1

        for i in range(n):
            pref *= nums[i]
            suff *= nums[n - i - 1]
            max_prod = max(max_prod, pref, suff)

            if pref == 0:
                pref = 1
            if suff == 0:
                suff = 1
        
        return max_prod

        
        # TLE Error
        # maxi=float("-inf")
        # for i in range(0,len(nums)):
        #     mul=1
        #     for j in range(i,len(nums)):
        #         mul *= nums[j]
        #         maxi=max(maxi,mul)
        # return maxi