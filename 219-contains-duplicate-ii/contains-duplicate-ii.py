class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # if len(nums)==len(set(nums)):
        #     return False
        # for i,n in enumerate(nums):
        #     if n in nums[i+1:i+k+1]:
        #         return True
        # return False


        hset = {}
        for idx in range(len(nums)):
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        return False


        # TLE ERROR
        # n=len(nums)
        # for i in range (n):
        #     for j in range(i+1,min(i+k+1,n)):
        #         if nums[i]==nums[j] and abs(i-j)<=k:
        #             return True
        # return False