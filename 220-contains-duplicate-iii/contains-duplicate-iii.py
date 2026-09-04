class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        """
        :type nums: List[int]
        :type indexDiff: int
        :type valueDiff: int
        :rtype: bool
        """
        k=indexDiff
        t=valueDiff
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False

        
        # n = len(nums)
        # for i in range(n):
        #     for j in range(i + 1, min(i + indexDiff + 1, n)):
        #         if abs(nums[i] - nums[j]) <= valueDiff:
        #             return True
        # return False

        # h1={}
        # for i in range(0,len(nums)):
        #     if nums[i] in h1:
        #         ind=h1[nums[i]]
        #         if abs(ind - i) <= indexDiff and abs(nums[ind] - nums[i]) <= valueDiff:
        #             return True
        #     h1[nums[i]]=i
        # return False

