class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        nums.sort()
        res=[]
        for i,value in enumerate(nums):
            if value==target:
                res.append(i)
        return res