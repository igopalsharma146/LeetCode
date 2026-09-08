class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for ch in asteroids:
            if ch>0:
                res.append(ch)
            else:
                while res and res[-1] >0 and res[-1]<abs(ch):
                    res.pop()
                if not res or res[-1]<0:
                    res.append(ch)
                elif res[-1] == abs(ch):
                    res.pop()
        return res