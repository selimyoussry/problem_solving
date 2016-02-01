class MyDate:

    def __init__(self, y=1900, m=1, d=1):
        """
        :type d: int
        :type m: int
        :type y: int
        :return:
        """
        self.m = m
        self.y = y
        self.d = d

    @staticmethod
    def month_days(month, leap_year):
        ret = 31
        if month in [9, 4, 6, 11]:
            ret = 30
        elif month == 2:
            ret = 29 if leap_year else 28
        return ret

    def is_leap_year(self):
        return ((self.y % 4 == 0) and (self.y % 100 != 0)) or (self.y % 400 == 0)

    def year_days(self):
        return 366 if self.is_leap_year() else 365

    def count_days_in_this_year(self):
        counter = 0
        leap_year = self.is_leap_year()
        for month in range(1, self.m):
            counter += self.month_days(month, leap_year)
        counter += self.d - 1

        return counter

def count_days(md1, md2):
    """
    :type md1: MyDate
    :type md2: MyDate
    :return:
    """

    counter = 0

    # Finish this year
    if md1.y < md2.y:
        counter += md1.year_days() - md1.count_days_in_this_year()

    # For every year in between, get the number of days
    for year in range(md1.y + 1, md2.y):
        tmp_md = MyDate(y=year)
        counter += tmp_md.year_days()

    # Now add the number of days until md2, in the same year
    counter += md2.count_days_in_this_year()

    return counter


def solve():

    # January 7th of 1900 was a Sunday
    ref_date = MyDate(
        y=1900,
        m=1,
        d=7
    )

    n_sundays = 0
    for year in range(1901, 2000 + 1):
        for month in range(1, 12 + 1):
            md = MyDate(
                y=year,
                m=month,
                d=1
            )

            if count_days(ref_date, md) % 7 == 0:
                n_sundays += 1

    return n_sundays
