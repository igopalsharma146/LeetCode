class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        d1={}
        for num in nums:
            d1[num]=d1.get(num,0)+1
        
        res=[]
        for key, value in d1.items():
            if value>1:
                res.append(key)
        return res