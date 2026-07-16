class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return min(nums)
        n=len(nums)
        left,right=0,n-1
        while left<right:
            mid=left+(right-left)//2

            if nums[mid]<nums[right]:
                right =mid
            elif nums[mid]>nums[right]:
                left=mid+1
            else:
                right -=1
        return nums[left]
