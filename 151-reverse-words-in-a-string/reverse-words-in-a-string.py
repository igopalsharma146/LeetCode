class Solution:
    def reverseWords(self, s: str) -> str:
        res=s.split()
        result=""
        n=len(res)
        for i in range(n-1,-1,-1):
            if n-1 > i:
                result+=" "
            result+=res[i]
        return result