class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s1=set()
        for ch in nums:
            if ch in s1:
                return ch
            s1.add(ch)