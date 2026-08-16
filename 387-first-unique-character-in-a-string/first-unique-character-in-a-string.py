class Solution:
    def firstUniqChar(self, s: str) -> int:
        d1={}
        for ch in s:
            d1[ch]=d1.get(ch,0)+1
        print(d1)
        
        i=0
        for ch in s:
            if d1[ch]==1:
                return i
            i+=1
        return -1