import requests
from classes.headhunter import HeadHunter
from classes.superjob import SuperJob
from classes.vacancies import Vacancy
from utils.format_vacancies import format_vacancies_hh, format_vacancies_sj


def getPage(page=0):
    """
    Создаем метод для получения страницы со списком вакансий.
    Аргументы:
        page - Индекс страницы, начинается с 0. Значение по умолчанию 0, т.е. первая страница
    """

    # Справочник для параметров GET-запроса
    params = {
        'text': 'NAME:Python',  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': 113,  # Поиск ощуществляется по вакансиям города Москва
        'page': page,  # Индекс страницы поиска на HH
        'per_page': 100,  # Кол-во вакансий на 1 странице
        'salary_from': 80000,
        'only_with_salary': 'true',
        'currency': 'RUR'
    }

    req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
    data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
    req.close()
    return data


# vac = SuperJob("ЪЪЪ", 100000)
# vac_g = vac.get_vacancies()
# format_vacancies_sj(vac_g)
# vac1 = HeadHunter("ЪЪЪ", 100000)
# vac1_g = vac1.get_vacancies()
# format_vacancies_hh(vac1_g)
# print(Vacancy.all_vacancies)

b = 0
a = b
b = 1
a = b
print(a)
