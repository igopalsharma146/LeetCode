class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(0,n):
            mini=i
            for j in range(i+1,n):
                if nums[j]<nums[mini]:
                    mini=j
            nums[mini],nums[i]=nums[i],nums[mini]
