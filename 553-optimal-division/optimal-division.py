class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        output=""
        for i in range(0,len(nums)):
            if i==1 and len(nums)>2:
                output+='('
            output+=str(nums[i])
            if i!=len(nums)-1:
                output+='/'
            if i==len(nums)-1 and len(nums)>2:
                output+=')'
        return output
            
