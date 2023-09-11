from classes.headhunter import HeadHunter
from classes.json_editor import JsonEditor
from classes.superjob import SuperJob
from classes.vacancies import Vacancy
from utils.format_vacancies import format_vacancies_hh, format_vacancies_sj


def user_interface():
    """
    Функция осуществляет взаимодействие с пользователем
    """
    json_editor = JsonEditor()
    json_editor.clear_file()
    while True:
        choice = input("Выберите платформу с которой хотите получить вакансии:\n"
                       "1 - HeadHunter, 2 - SuperJob 3 - HeadHunter&SuperJob 4 - Выход:\n")
        if choice == '1':
            search_query = input("Введите ключевое слово вакансии: ")
            salary = int(input("Можете ввести желаемый уровень зарплаты "))
            show_salary = int(input("0 - показать все вакансии"
                                    " 1 - показать только вакансии с указанной зарплатой "))
            hh_api = HeadHunter(search_query=search_query, salary=salary, show_salary=bool(show_salary))
            get_hh = hh_api.get_vacancies()
            format_vacancies_hh(get_hh)
            vacancies = Vacancy.all_vacancies
            json_editor.add_vacancy(vacancies)
            if len(vacancies) == 0:
                print("Такой вакансии нет")
        elif choice == '2':
            search_query = input("Введите ключевое слово вакансии: ")
            salary = int(input("Можете ввести желаемый уровень зарплаты "))
            show_salary = int(input("0 - показать все вакансии"
                                    "1 - показать только вакансии с указанной зарплатой "))
            sj_api = SuperJob(search_query=search_query, salary=salary, show_salary=show_salary)
            get_sj = sj_api.get_vacancies()
            format_vacancies_sj(get_sj)
            vacancies = Vacancy.all_vacancies
            json_editor.add_vacancy(vacancies)
            if len(vacancies) == 0:
                print("Такой вакансии нет")
            else:
                top_n = int(input("Введите количество вакансий для вывода: "))

        elif choice == '3':
            search_query = input("Введите ключевое слово вакансии: ")
            salary = int(input("Можете ввести желаемый уровень зарплаты "))
            show_salary = int(input("0 - показать все вакансии"
                                    "1 - показать только вакансии с указанной зарплатой "))
            sj_api = SuperJob(search_query=search_query, salary=salary, show_salary=show_salary)
            get_sj = sj_api.get_vacancies()
            format_vacancies_sj(get_sj)
            hh_api = HeadHunter(search_query=search_query, salary=salary, show_salary=bool(show_salary))
            get_hh = hh_api.get_vacancies()
            format_vacancies_hh(get_hh)
            vacancies = Vacancy.all_vacancies
            json_editor.add_vacancy(vacancies)
            if len(vacancies) == 0:
                print("Такой вакансии нет")
        elif choice == '4':
            print("Удачного дня")
            break
        else:
            print("Ошибочный запрос!")


def sort_vacancies_by_salary(vacancies, top_n):
    """
    Сортирует вакансии по зарплате и выводит в консоль
    :param vacancies: список вакансий
    :param top_n: число вакансий для вывода в консоль
    :return:
    """

    def key_to_sort(key):
        """
        Задаёт ключ для сортировки
        :param key: ключ сортировки
        :return: ключ
        """
        return key["salary_from"]

    vacancies.sort(key=key_to_sort, reverse=True)
    if top_n > len(vacancies):
        top_n = len(vacancies)
    sorted_vacancies = vacancies[:top_n]
    for vacancy in sorted_vacancies:
        print(f"""{vacancy['title']}
{vacancy['desc']}
{vacancy['employer']}
{vacancy['salary_from']}
{vacancy['salary_to']}
{vacancy['url']}""")
