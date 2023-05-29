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
    hh_flag = False
    sj_flag = False

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

        hh_flag = True

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

        sj_flag = True

    while True:

        command = input("Введите команду:\n"
                        "select - выбрать вакансии с зарплатой от ____\n"
                        "sort - отсортировать вакансии по повышению зарплаты\n"
                        "top - показать ТОП вакансий по зарплате\n"
                        "delete - удалить вакансии без указания зарплаты\n")

        if command == "sort":
            sorted_vacancies = sorting(all_vacancies)

            for vacancy in sorted_vacancies:
                print(vacancy)

        elif command == "top":
            try:
                top_count = int(input("Введите количество вакансий для вывода: "))
            except ValueError:
                print("Количество должно быть числом.\n")
                continue

            top_vacancies = get_top(all_vacancies, top_count)
            for vacancy in top_vacancies:
                print(vacancy)

        elif command == "select":
            try:
                request_salary = int(input("Введите минимальную зарплату: "))
            except ValueError:
                print("Неправильный формат введенной зарплаты\n")
                continue

            salary_selected_list = []

            if hh_flag:
                hh_sel = get_hh_selected_salary_list(hh_saver, request_salary)
                salary_selected_list += hh_sel

            if sj_flag:
                sj_sel = get_sj_selected_salary_list(sj_saver, request_salary)
                salary_selected_list += sj_sel

            salary_selected_list.sort()

            for vacancy in salary_selected_list:
                print(vacancy)

        elif command == "delete":

            salary_deleted_list = []

            if hh_flag:
                hh_saver.delete({"salary": None})
                del_hh_saver = hh_engine.get_json_saver("parsed_data/hh_vacancies.json")
                del_hh_list = get_hh_vacancies_list(del_hh_saver)
                salary_deleted_list += del_hh_list

            if sj_flag:
                sj_saver.delete({"payment_from": 0})
                del_sj_saver = sj_engine.get_json_saver("parsed_data/sj_vacancies.json")
                del_sj_list = get_sj_vacancies_list(del_sj_saver)
                salary_deleted_list += del_sj_list

                salary_deleted_list.sort()

            for vacancy in salary_deleted_list:
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
