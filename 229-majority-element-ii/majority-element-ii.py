class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        more_than=len(nums)//3
        freq={}
        for ch in nums:
            freq[ch]=freq.get(ch,0)+1
        
        res=[]
        for ch in freq:
            if freq[ch]>more_than:
                res.append(ch)
        return res