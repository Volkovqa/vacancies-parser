from src.vacancy_classes import Vacancy
from src.vacancy_classes import HHVacancy
from src.vacancy_classes import SJVacancy


def sorting(vacancies: list[Vacancy]) -> list[Vacancy]:
    return sorted(vacancies)


def get_top(vacancies: list[Vacancy], top_count: int) -> list[Vacancy]:
    return list(sorted(vacancies, reverse=True)[:top_count])


def get_hh_vacancies_list(saver) -> list[HHVacancy]:
    vacancies = [

        HHVacancy(
            title=vacancy["name"],
            link=vacancy["alternate_url"],
            description=vacancy["snippet"],
            salary=vacancy["salary"]["from"] if vacancy.get("salary") else None)

        for vacancy in saver.select()]

    return vacancies


def get_sj_vacancies_list(saver) -> list[SJVacancy]:
    vacancies = [

        SJVacancy(
            title=vacancy["profession"],
            link=vacancy["link"],
            description=vacancy["candidat"],
            salary=vacancy["payment_from"])

        for vacancy in saver.select()]

    return vacancies
