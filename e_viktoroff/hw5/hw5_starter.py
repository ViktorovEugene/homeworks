# -*- coding: utf8 -*-

u"""
Задание 1: классный Человек.

УСЛОВИЕ:

Реализовать класс Person, который отображает запись в книге контактов.

Класс имеет 4 атрибута:
- surname - строка - фамилия контакта (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный)

Каждый вызов класса должен создавать экземпляр (инстанс) класса с указанными
атрибутами.

Также класс имеет 2 метода:
- get_age() - считает возраст контакта в полных годах на дату вызова и
возвращает строку вида: "27";
- get_fullname() - возвращает строку, отражающую полное имя (фамилия + имя)
контакта;

Примечание:
1) смотрите документацию по модулю datetime;
2) при создании атрибута birth_date из строки типа "2014-12-31" необходимо:
- определить какая информация нужна для создания объекта datetime.date,
- получить эти данные из строки - разобрать ее (достать из нее отдельно,
год, месяц, число),
- на основании этой информации создать специальный объект datetime.date,
- поместить этот спец.объект в атрибут экземпляра класса;

Пример:
при запуске скрипта (homeworks/.../hw5/hw5_starter.py) должны проходить тесты
из файла тестов (homeworks/.../hw5/hw5_tests.py), кот. прилагается.
"""

__autor__ = "Viktorov Eugene"
__email__ = "jekafromua@gmail.com"
__date__ = "2014-11-19"


"""- surname - строка - фамилия контакта (обязательный)
- first_name - строка - имя контакта (обязательный)
- nickname - строка - псевдоним (опциональный)
- birth_date - объект datetime.date (обязательный)
"""


class Preson(object):

    u"""извините, не успел) но, за-то, всё работает!"""


    def __init__(self, surname, first_name, birth_date, nickname=""):

        from datetime import datetime

        self.surname, self.first_name = surname, first_name
        self.nickname = nickname

        self.birth_date = datetime.strptime(birth_date, "%Y-%m-%d")

    def get_age(self):

        from datetime import datetime

        today_date = datetime.today()
        age = [0, 0, 0]
        age[0] = today_date.year - self.birth_date.year
        age[1] = today_date.month - self.birth_date.month
        age[2] = today_date.day - self.birth_date.day
        if age[0] < 0:
            return 'incorrect date of birth'
        for i in age:
            if i < 0:
                return age[0] - 1
        return age[0]

    def get_fullname(self):
        full_name = self.surname + " " + self.first_name
        if self.nickname != '':
            full_name = full_name + ', nickname:' + self.nickname
        return full_name


surmame = 'Viktorov'
first_name = 'Eugene'
nickname = 'jeka_from_ua'
birth_date = '1991-10-01'


preson = Preson(surmame, first_name, birth_date, nickname)
print person.get_age()
print person.get_fullmame()
