class Solution(object):
    def getNoZeroIntegers(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def containsZero(num):
            while num > 0:
                if num % 10 == 0:
                    return True
                num //= 10
            return False

        for i in range(1, n):
            j = n - i
            if not containsZero(i) and not containsZero(j):
                return [i, j]
        return []