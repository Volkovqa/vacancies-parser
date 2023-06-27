from src.vacancy_classes import Vacancy
from src.vacancy_classes import HHVacancy
from src.vacancy_classes import SJVacancy


def sorting(vacancies: list[Vacancy]) -> list[Vacancy]:

    """Метод для сортировки списка вакансий по зарплате. В классе Vacancy описан магический метод сортировки."""

    return sorted(vacancies)


def get_top(vacancies: list[Vacancy], top_count: int) -> list[Vacancy]:

    """Метод для получения самых высокооплачиваемых вакансий из парсенного списка с вакансиями."""

    return list(sorted(vacancies, reverse=True)[:top_count])


def get_hh_vacancies_list(saver) -> list[HHVacancy]:

    """Метод для преобразования информации о вакансиях, записанной в файл, в список экземпляров класса Vacancy."""

    vacancies = [

        HHVacancy(
            title=vacancy["name"],
            link=vacancy["alternate_url"],
            description=vacancy["snippet"],
            salary=vacancy["salary"]["from"] if vacancy.get("salary") else None)

        for vacancy in saver.select()]

    return vacancies


def get_sj_vacancies_list(saver) -> list[SJVacancy]:

    """Метод для преобразования информации о вакансиях, записанной в файл, в список экземпляров класса Vacancy."""

    vacancies = [

        SJVacancy(
            title=vacancy["profession"],
            link=vacancy["link"],
            description=vacancy["candidat"],
            salary=vacancy["payment_from"])

        for vacancy in saver.select()]

    return vacancies


def get_hh_selected_salary_list(saver, param: int) -> list[HHVacancy]:

    """Метод для выборки из файла вакансий, соответствующих зарплатным ожиданиям пользователя."""

    if not isinstance(param, int):
        return "Зарплата должна быть указана целым числом"
    else:
        vacancies = [

            HHVacancy(
                title=vacancy["name"],
                link=vacancy["alternate_url"],
                description=vacancy["snippet"],
                salary=vacancy["salary"]["from"] if vacancy.get("salary") else None)

            for vacancy in saver.select() if vacancy.get("salary") and vacancy["salary"]["from"] >= param]

        return vacancies


def get_sj_selected_salary_list(saver, param: int) -> list[SJVacancy]:

    """Метод для выборки из файла вакансий, соответствующих зарплатным ожиданиям пользователя."""

    if not isinstance(param, int):
        return "Зарплата должна быть указана целым числом"
    else:
        vacancies = [

            SJVacancy(
                title=vacancy["profession"],
                link=vacancy["link"],
                description=vacancy["candidat"],
                salary=vacancy["payment_from"])

            for vacancy in saver.select() if vacancy["payment_from"] is not None and vacancy["payment_from"] >= param]

        return vacancies
