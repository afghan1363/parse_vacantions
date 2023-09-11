import json
import requests
from classes.abstractclass import GetVacancies


class SuperJob(GetVacancies):
    """Получение вакансий в формате json
     с сайта superjob.ru"""

    def __init__(self, search_query, salary=None, show_salary=0):
        self.search_query = search_query
        self.salary = salary
        self.show_salary = show_salary

    def get_vacancies(self):
        """Метод для отправки запроса"""
        headers_sj = {
            "X-Api-App-Id": "v3.h.4525045.ed10e2c364a8b30ec575f46690c"
                            "d3eb9519ed323.3032a7eabfb8d5c94df31d600f62a208445dfd98"
        }
        superjob_api = 'https://api.superjob.ru/2.0/vacancies'

        params = {
            "keyword": self.search_query,
            'payment_from': self.salary,  # зарплата from и to
            'is_archive': False,  # id open name Открытая
            'payment_defined': self.show_salary
        }

        req = requests.get(superjob_api, headers=headers_sj, params=params)
        data = req.content.decode()
        req.close()
        sj_json = json.loads(data)
        return sj_json
