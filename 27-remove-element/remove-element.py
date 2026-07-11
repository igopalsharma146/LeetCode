class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        n=len(nums)
        i=0
        while i<n and nums[i]!=val:
            i+=1
        
        j=i+1
        while j<n:
            if nums[j]!=val:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
            j+=1
        return i