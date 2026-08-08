class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        total_days = 0
        for i in range(1, month):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                total_days += 31

            elif i == 2:
                if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                    total_days += 29
                else:
                    total_days += 28

            else:
                total_days += 30

        return total_days + day