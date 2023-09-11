import json
import requests
from classes.abstractclass import GetVacancies


class HeadHunter(GetVacancies):
    """Получение вакансий в формате json
    с сайта hh.ru"""

    def __init__(self, search_query, salary=None, show_salary=False):
        self.search_query = search_query
        self.salary = salary
        self.show_salary = show_salary

    def get_vacancies(self):
        """
        Метод для отправки запроса
        """
        params = {
            'text': self.search_query,  # Текст фильтра.
            'area': 113,  # Поиск осуществляется по вакансиям России
            'per_page': 100,  # Кол-во вакансий на 1 странице
            'salary': self.salary,
            'only_with_salary': self.show_salary,
            'currency': 'RUR'
        }
        req = requests.get('https://api.hh.ru/vacancies', params)  # Посылаем запрос к API
        data = req.content.decode()  # Декодируем его ответ, чтобы Кириллица отображалась корректно
        req.close()
        hh_json = json.loads(data)
        return hh_json
