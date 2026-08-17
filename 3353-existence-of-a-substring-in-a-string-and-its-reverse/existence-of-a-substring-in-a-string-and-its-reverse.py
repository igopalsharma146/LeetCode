class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        rev=s[::-1]
        i,j=0,1
        while j<len(s):
            ch=s[i]+s[j]
            if ch in rev:
                return True
            i+=1
            j+=1
        return False