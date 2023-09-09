import json

import requests

from classes.headhunter import HeadHunter
from classes.superjob import SuperJob


def hello():
    keyword = input("Введите ключевое слово названия вакансии ")
    salary = input("Введите желаемую вилку зарплаты ")
    hh = HeadHunter()
    sj = SuperJob()
    hh.get_vacancies(keyword=keyword, salary=salary)
    sj.get_vacancies(keyword=keyword, salary=salary)

hello()


