class Solution:
    def check(self, nums: List[int]) -> bool:
        left,right=0,1
        while right<len(nums):
            if nums[left]>nums[right]:
                break
            left+=1
            right+=1

        if right==len(nums):
            return True
        
        res=nums[right:]+nums[:right]
        nums.sort()
        if res==nums:
            return True
        else:
            return False
