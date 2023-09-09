import json
import requests
from classes.abstractclass import GetVacancies


class SuperJob(GetVacancies):

    def get_vacancies(self, search_query, salary):
        headers_sj = {
            "X-Api-App-Id": "v3.h.4525045.ed10e2c364a8b30ec575f46690cd3eb9519ed323.3032a7eabfb8d5c94df31d600f62a208445dfd98"
        }
        superjob_api = 'https://api.superjob.ru/2.0/vacancies'

        params = {
            "keyword": search_query,
            'id_vacancy': None,  # ID вакансии
            'profession': None,  # назввние должности
            'payment_from': salary,  # зарплата from и to
            'is_archive': False,  # id open name Открытая
            'title_client': None,  # имя работодателя
            'experience': None,  # нет опыта
            'type_of_work': None,  # занятость полная_неполная
            'vacancyRichText': None,  # описание
            'candidat': None  # требования
        }

        response = requests.get(superjob_api, headers=headers_sj, params=params)
        data = response.content.decode()
        sj_json = json.loads(data)

        pass
