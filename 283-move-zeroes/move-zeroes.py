class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        j = 0 # Pointer to place the next non-zero element
        for i in range(len(nums)):
            if nums[i] != 0:
                # Swap current element with the element at index j 
                nums[i], nums[j] = nums[j], nums[i]
                j += 1 # Move j to the next index for placing non-zero

        # i=0
        # n=len(nums)
        # while i<n:
        #     if nums[i] == 0:
        #         break
        #     i+=1
        
        # j=i+1
        # while j<n:
        #     if nums[j] == 0:
        #         j+=1
        #         continue
        #     else:
        #         nums[j],nums[i]=nums[i],nums[j]
        #         i+=1
        #     j+=1
        
