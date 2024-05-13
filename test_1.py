import re


class Date:
    def __init__(self, date):
        self.__date = self.chek_date(date)

    def chek_date(self, date):

        pattern = re.compile(r'^(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[012])\.\d{4}$')

        if pattern.match(date):

            day = int(date[:2])
            month = int(date[3:5])
            year = int(date[6:])
            leap_year = self.is_leap_year(year)

            if month in [4, 6, 9, 11] and day > 30:
                print('ошибка')
                return None
            elif leap_year and month == 2 and day > 29:
                print('ошибка')
                return None
            elif not leap_year and month == 2 and day > 28:
                print('ошибка')
                return None
            return date
        print('ошибка')
        return None

    @property
    def date(self):
        if self.__date != None:
            day = int(self.__date[:2])
            month = self.__date[3:5]
            year = int(self.__date[6:])
            months = {
                '01': 'янв',
                '02': 'фев',
                '03': 'мар',
                '04': 'апр',
                '05': 'май',
                '06': 'июн',
                '07': 'июл',
                '08': 'авг',
                '09': 'сен',
                '10': 'окт',
                '11': 'ноя',
                '12': 'дек'
            }
            return f'{day} {months[month]} {year} г.'
        return None

    @date.setter
    def date(self, date):
        self.__date = self.chek_date(date)

    def is_leap_year(self, year):
        return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

    def to_timestamp(self):
        day_sec = 24 * 60 * 60
        day = int(self.__date[:2])
        month = int(self.__date[3:5])
        year = int(self.__date[6:])
        summ = 0
        for i in range(1970, year):
            if self.is_leap_year(i):
                summ += 31622400
            else:
                summ += 31536000
        for i in range(1, month):
            if i == 2 and self.is_leap_year(year):
                summ += 29 * day_sec
            elif i == 2 and not self.is_leap_year(year):
                summ += 28 * day_sec
            elif i in [4, 6, 9, 11]:
                summ += 30 * day_sec
            else:
                summ += 31 * day_sec
        summ += (day - 1) * day_sec
        return summ

    def __lt__(self, other):
        return self.to_timestamp() < other.to_timestamp()

    def __le__(self, other):
        return self.to_timestamp() <= other.to_timestamp()

    def __eq__(self, other):
        return self.to_timestamp() == other.to_timestamp()

    def __ne__(self, other):
        return self.to_timestamp() != other.to_timestamp()

    def __gt__(self, other):
        return self.to_timestamp() > other.to_timestamp()

    def __ge__(self, other):
        return self.to_timestamp() >= other.to_timestamp()

    def __str__(self):
        return f'{self.__date}'



