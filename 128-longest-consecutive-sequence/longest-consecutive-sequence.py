class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s1=set(nums)
        maxi=0
        for ch in s1:
            count=1
            if ch-1 not in s1:
                while ch+1 in s1:
                    count+=1
                    ch+=1
            maxi=max(maxi,count)
        return maxi