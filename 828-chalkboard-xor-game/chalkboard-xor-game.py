class Solution(object):
    def xorGame(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        test= 0
        for n in nums:
            test = test ^ n

        n=len(nums)
        return True if test == 0 else n % 2 == 0