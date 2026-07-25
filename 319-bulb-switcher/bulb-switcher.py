class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)

        # for 1th bulb : 1
        #     2nd : 1 0
        #     3rd : 1 0 0
        #     4th : 1 0 0 1
        #     5th : 1 0 0 1 0
        #     6th : 1 0 0 1 0 0
        #     7th : 1 0 0 1 0 0 0
        #     8th : 1 0 0 1 0 0 0 0
        #     9th : 1 0 0 1 0 0 0 0 1