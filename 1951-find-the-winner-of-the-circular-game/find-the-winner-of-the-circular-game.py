class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l1=[]
        for i in range(1,n+1):
            l1.append(i)

        i=0
        while len(l1) > 1:
            e= (i+k-1) % len(l1)
            l1.pop(e)
            i=e
        return l1[0]
                