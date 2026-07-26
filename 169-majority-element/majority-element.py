class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # d1={}
        # for num in nums:
        #     d1[num]=d1.get(num,0)+1
        
        # count=float("-inf")
        # maxi=None
        # for value in d1:
        #     if d1[value]>count:
        #         count=d1[value]
        #         maxi=value
        # return maxi

        nums.sort()
        n=len(nums)
        return nums[n//2]