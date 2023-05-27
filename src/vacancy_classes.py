class Vacancy:

    __slots__ = ["__title", "__link", "__description", "__salary"]

    def __init__(self, title, link, description, salary) -> None:
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__slots__})"

    def __str__(self):
        return self.title

    def __gt__(self, other):
        return self.salary > other.salary

    def __lt__(self, other):

        if other.salary is None:
            return False
        if self.salary is None:
            return True

        return self.salary < other.salary

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if isinstance(value, str):
            self.__title = value

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, value):
        if isinstance(value, str):
            self.__link = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if isinstance(value, str):
            self.__description = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, (int, type(None))):
            self.__salary = value


class HHVacancy(Vacancy):

    def __str__(self):
        return f"HH: {self.title}, зарплата: {self.salary} руб/мес"


class SJVacancy(Vacancy):

    def __str__(self):
        return f"SJ: {self.title}, зарплата: {self.salary} руб/мес"
