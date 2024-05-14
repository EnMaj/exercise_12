class Meeting:
    lst_meeting = []

    def __init__(self, id, date, title):
        self.__id = id
        self.__date = date
        self.__title = title
        self.__employees = []
        Meeting.lst_meeting.append(self)

    @property
    def date(self):
        return self.__date

    @property
    def id(self):
        return self.__id

    @property
    def employees(self):
        return self.__employees

    def add_person(self, person):
        self.__employees.append(person)

    def count(self):
        return len(self.__employees)

    @classmethod
    def count_meeting(cls, date):
        count = 0
        for meeting in cls.lst_meeting:
            if str(meeting.date) == str(date):
                count += 1
        return count

    @classmethod
    def total(cls):
        count = 0
        for meeting in cls.lst_meeting:
            count += len(meeting.employees)
        return count

    def __repr__(self):
        result = f'Рабочая встреча {self.__id}\n {self.__date} {self.__title}\n'
        for employee in self.__employees:
            result += str(employee) + '\n'
        return result


class User:
    people = []

    def __init__(self, id, nick_name, first_name, last_name, middle_name, gender):
        self.__id = id
        self.__nick_name = nick_name
        self.__first_name = first_name
        self.__last_name = last_name
        self.__middle_name = middle_name
        self.__gender = gender
        User.people.append(self)

    @property
    def id(self):
        return self.__id

    def __repr__(self):
        if self.__gender != '':
            return (
                f'ID: {self.__id} LOGIN:{self.__nick_name} NAME:{self.__last_name} {self.__first_name} {self.__middle_name} '
                f'GENDER:{self.__gender}')
        return f'ID: {self.__id} LOGIN:{self.__nick_name} NAME:{self.__last_name} {self.__first_name} {self.__middle_name} '


class Date:
    months = {
        1: 'янв',
        2: 'фев',
        3: 'мар',
        4: 'апр',
        5: 'май',
        6: 'июн',
        7: 'июл',
        8: 'авг',
        9: 'сен',
        10: 'окт',
        11: 'ноя',
        12: 'дек'
    }

    def __init__(self, date):
        self.__day = date[:2]
        self.__month = Date.months[int(date[3:5])]
        self.__year = date[6:]

    def __repr__(self):
        return f'{self.__day} {self.__month} {self.__year} г.'


class Load:
    data = []

    @staticmethod
    def write(meetings, persons, pers_meetings):
        with open(meetings, 'r', encoding='utf8') as meetings_file:
            for line in meetings_file:
                id, date, title = line.rstrip()[:-1].split(';')
                if date != 'date':
                    new_meeting = Meeting(id, Date(date), title)

        with open(persons, 'r', encoding='utf8') as persons_file:
            for line in persons_file:
                id, nick_name, first_name, last_name, middle_name, gender = line.rstrip()[:-1].split(';')
                new_person = User(id, nick_name, first_name, last_name, middle_name, gender)

        with open(pers_meetings, 'r', encoding='utf8') as pers_meetings_file:
            for line in pers_meetings_file:
                id_meet, id_pers = line.rstrip()[:-1].split(';')
                for person in User.people:
                    if person.id == id_pers:
                        for meeting in Meeting.lst_meeting:
                            if meeting.id == id_meet:
                                meeting.add_person(person)


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))
