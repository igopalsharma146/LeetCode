class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d1={}
        for num in  nums:
            d1[num]=d1.get(num,0)+1
        
        d1=dict(sorted(d1.items(), key=lambda x:x[1], reverse=True))
        res=[]
        for key, value in d1.items():
            if len(res)==k:
                return res
            res.append(key)
        return res