class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        def int_to_bin(n,k):
            count=0
            while n:
                rem=n%2
                if rem==1:
                    count+=1
                n=n//2
            return count==k
        res=0
        n=len(nums)
        for i in range(0,n):
            if int_to_bin(i,k):
                res+=nums[i]
        return res