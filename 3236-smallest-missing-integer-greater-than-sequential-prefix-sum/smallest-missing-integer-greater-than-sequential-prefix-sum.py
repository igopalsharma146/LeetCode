class Solution(object):
    def missingInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first=nums[0]
        i=1
        sum1=first
        while i<len(nums):
            if nums[i] == nums[i-1] + 1:
                sum1 += nums[i]
            else:
                break
            i += 1
        
        while True:
            if sum1 not in nums:
                return sum1
            sum1 += 1