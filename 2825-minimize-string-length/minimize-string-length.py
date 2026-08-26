class Solution:
    def minimizedStringLength(self, s: str) -> int:
        f1={}
        for ch in s:
            f1[ch]=f1.get(ch,0)+1
        return len(f1)