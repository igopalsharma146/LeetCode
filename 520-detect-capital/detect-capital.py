class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        CapitalLetter=0
        LowerLetter=0
        n=len(word)
        for ch in word:
            if 65<=ord(ch)<=90:
                CapitalLetter+=1
            elif 97<=ord(ch)<=122:
                LowerLetter+=1
        if CapitalLetter==n or LowerLetter==n or (65<=ord(word[0])<=90 and LowerLetter==n-1):
            return True
        else:
            return False
            