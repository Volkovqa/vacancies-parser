from src.api_classes import HHru, SuperJob
from src.utils import *


def main():

    print("Привет. "
          "Эта консольная программа поможет Вам выгрузить и отсортировать интересующие Вас вакансии с платформ"
          "HeadHunter и SuperJob")

    while True:
        choose_platform = input("Введите команду, с каких платформ вы хотите выгрузить вакансии или exit для выхода:\n"
                                "HH - HeadHunter\n"
                                "SJ - SuperJob\n"
                                "HS - HeadHunter и SuperJob\n"
                                "exit - выход из программы\n")

        if choose_platform == "exit":
            exit()

        elif choose_platform.lower() in ("hh", "sj", "hs"):
            break

        else:
            print("Неправильная команда")

    keyword = input("Введите ключевое слово для поиска вакансий: ")

    all_vacancies = []
    all_savers = []

    if choose_platform.lower() in ("hh", "hs"):

        hh_engine = HHru(keyword)
        hh_saver = hh_engine.get_json_saver("parsed_data/hh_vacancies.json")

        for page in range(1):

            hh_vacancies = hh_engine.get_request().json()["items"]
            for vacancy in hh_vacancies:
                hh_saver.insert(vacancy)

        all_savers.append(hh_saver)
        hh_vacancies = get_hh_vacancies_list(hh_saver)
        all_vacancies += hh_vacancies

    if choose_platform.lower() in ("sj", "hs"):
        sj_engine = SuperJob(keyword)
        sj_saver = sj_engine.get_json_saver("parsed_data/sj_vacancies.json")

        for page in range(1):

            sj_vacancies = sj_engine.get_request().json()["objects"]
            for vacancy in sj_vacancies:
                sj_saver.insert(vacancy)

        all_savers.append(sj_saver)
        sj_vacancies = get_sj_vacancies_list(sj_saver)
        all_vacancies += sj_vacancies

    while True:

        command = input("Введите команду (sort или top): ")

        if command == "sort":
            sorted_vacancies = sorting(all_vacancies)

            for vacancy in sorted_vacancies:
                print(vacancy)

        elif command == "top":
            top_count = int(input("Введите количество вакансий для вывода: "))

            top_vacancies = get_top(all_vacancies, top_count)
            for vacancy in top_vacancies:
                print(vacancy)

        else:
            print("Некорректная команда. Попробуйте еще раз.")

        continue_running = input("Хотите продолжить работу с программой? (y/n): ")

        if continue_running.lower() == "n":

            for saver in all_savers:
                saver.clear_data()

            break


if __name__ == "__main__":
    main()
