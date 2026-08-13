class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        freq={}
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1
            if freq[ch]>=2:
                return True
        return False