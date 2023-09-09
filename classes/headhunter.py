import requests

from classes.abstractclass import GetVacancies


class HeadHunter(GetVacancies):

    def get_vacancies(self, name, keyword, salary=None):
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

    def format_vacancies(self, keyword, salary=None):
        pass
