from src.api_classes import HHru, SuperJob
from src.utils import *


def main():

    keyword = input("Введите ключевое слово для поиска вакансий: ")

    hh_engine = HHru(keyword)
    sj_engine = SuperJob(keyword)

    hh_saver = hh_engine.get_json_saver("parsed_data/hh_vacancies.json")
    sj_saver = sj_engine.get_json_saver("parsed_data/sj_vacancies.json")

    for page in range(1):

        hh_vacancies = hh_engine.get_request().json()["items"]
        for vacancy in hh_vacancies:
            hh_saver.insert(vacancy)

        sj_vacancies = sj_engine.get_request().json()["objects"]
        for vacancy in sj_vacancies:
            sj_saver.insert(vacancy)

    while True:

        command = input("Введите команду (sort или top): ")

        if command == "sort":

            hh_vacancies = get_hh_vacancies_list(hh_saver)
            sj_vacancies = get_sj_vacancies_list(sj_saver)

            sorted_vacancies = sorting(hh_vacancies + sj_vacancies)

            for vacancy in sorted_vacancies:
                print(vacancy)

        elif command == "top":

            hh_vacancies = get_hh_vacancies_list(hh_saver)
            sj_vacancies = get_sj_vacancies_list(sj_saver)

            all_vacancies = hh_vacancies + sj_vacancies

            top_count = int(input("Введите количество вакансий для вывода: "))

            top_vacancies = get_top(all_vacancies, top_count)
            for vacancy in top_vacancies:
                print(vacancy)

        else:
            print("Некорректная команда. Попробуйте еще раз.")

        continue_running = input("Хотите продолжить работу с программой? (y/n): ")

        if continue_running.lower() == "n":

            hh_saver.clear_data()
            sj_saver.clear_data()

            break


if __name__ == "__main__":
    main()
