class Solution:
    def frequencySort(self, s: str) -> str:
        d1={}
        for ch in s:
            d1[ch]=d1.get(ch,0)+1
        
        res=''
        for key,value in sorted(d1.items(), key=lambda x:x[1], reverse=True):
            res+=key*value
        return res