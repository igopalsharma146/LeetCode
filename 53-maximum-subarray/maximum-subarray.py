class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i,total=0,0
        maxi=float("-inf")
        while i<len(nums):
            total+=nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
            i+=1
        return maxi