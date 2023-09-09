import requests

from classes.abstractclass import GetVacancies


class HeadHunter(GetVacancies):

    def get_vacancies(self, name, keyword, salary=None):

        params = {'text': keyword,
                  'per_page': 100,
                  'only_with_salary': 'true',
                  'salary': salary}



    def format_vacancies(self, keyword, salary=None):
        pass
