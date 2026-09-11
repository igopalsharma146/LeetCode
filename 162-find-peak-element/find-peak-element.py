class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        peak=None
        for i in range(0,len(nums)):
            if i==0 and i < len(nums)-1 and nums[i] > nums[i+1]:
                peak=i
            if i>0 and i < len(nums)-1:
                if nums[i-1]< nums[i] > nums[i+1]:
                    return i
            if i>0 and i==len(nums)-1 and nums[i-1]<nums[i]:
                peak=i
        return peak