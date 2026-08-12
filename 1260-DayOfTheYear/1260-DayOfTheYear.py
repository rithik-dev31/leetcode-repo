# Last updated: 8/12/2026, 11:27:51 AM
class Solution(object):
    def dayOfYear(self, date):
        year, month, day = map(int, date.split("-"))

        days = [31, 28, 31, 30, 31, 30,
                31, 31, 30, 31, 30, 31]

        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            days[1] = 29

        total = day

        for i in range(month - 1):
            total += days[i]

        return total