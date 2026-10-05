class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = []
        used = [False] * n

        def solve(subset):
            if len(res) == k:
                return

            if len(subset) == n:
                res.append(subset[:])
                return

            for i in range(n):
                if used[i]:
                    continue

                subset.append(i + 1)
                used[i] = True

                solve(subset)

                subset.pop()
                used[i] = False

                if len(res) == k:
                    return

        solve([])

        if len(res) < k:
            return ""

        return "".join(map(str, res[k - 1]))