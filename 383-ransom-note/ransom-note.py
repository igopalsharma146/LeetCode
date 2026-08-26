class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        f1={}
        for ch in ransomNote:
            f1[ch]=f1.get(ch,0)+1
        
        f2={}
        for ch in magazine:
            f2[ch]=f2.get(ch,0)+1

        for key,val in f1.items():
            if key not in f2:
                return False
            if f2[key]<f1[key]:
                return False
        return True