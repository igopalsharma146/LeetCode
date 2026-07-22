class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        while i<n:
            if nums[i] == 0:
                break
            i+=1
        
        j=i+1
        while j<n:
            if nums[j] == 0:
                j+=1
                continue
            else:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            j+=1
        
