class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res = []
        ans = ""

        for ch in s:
            if ch.isdigit():
                ans += ch
            else:
                if not ans:
                    continue

                if res and res[-1] >= int(ans):
                    return False
                res.append(int(ans))
                ans = ""           
        if ans:
            if res and res[-1] >= int(ans):
                return False
        return True

        # s = s.split(" ")
        # count = -1
        # for i in s:
        #     if i.isdigit():
        #         if count == int(i):
        #             return False
        #         elif count > int(i):
        #             return False
        #         else:
        #             count = int(i)
        # return True
