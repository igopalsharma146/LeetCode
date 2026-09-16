class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l1=[]
        for i in range(1,n+1):
            l1.append(i)

        i=0
        while len(l1) > 1:
            i= (i+k-1) % len(l1)
            l1.pop(i)
        return l1[0]
                