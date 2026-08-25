class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s1=set(nums)
        i=1
        while i:
            if k*i not in s1:
                return k*i
            i+=1