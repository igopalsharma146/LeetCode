class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first,second,third=float("-inf"),float("-inf"),float("-inf")
        for num in nums:
            if num>first:
                third=second
                second=first
                first=num
            elif num<first and num>second:
                third=second
                second=num
            elif num<second and num>third:
                third=num
        print(first,second,third)
        if third == float("-inf"):
            return first
        return third