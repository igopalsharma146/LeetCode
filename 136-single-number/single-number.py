class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict1={}
        for num in nums:
            dict1[num]=dict1.get(num,0)+1
        
        for num in nums:
            if dict1[num]==1:
                return num
                