class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        res=None
        for ch in matrix:
            if not res:
                res=ch
            else:
                res.extend(ch)
        res.sort()
        return res[k-1]