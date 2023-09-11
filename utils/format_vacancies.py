from classes.vacancies import Vacancy


def format_vacancies_hh(data):
    for el in data['items']:
        if not el['salary']:
            el['salary'] = {}
        title = el['name']
        desc = el['snippet']['responsibility']
        salary_from = el['salary'].get('from', 0)
        salary_to = el['salary'].get('to', 0)
        url = el['apply_alternate_url']
        employer = el['employer']['name']
        vacancy = Vacancy(title, desc, salary_from, salary_to, url, employer)


def format_vacancies_sj(data):
    # vac_sj = []
    # data = self.get_vacancies()
    for el in data['objects']:
        title = el['profession']
        desc = el['candidat']
        salary_from = el['payment_from']
        salary_to = el['payment_to']
        url = el['link']
        employer = el['firm_name']
        vacancy = Vacancy(title, desc, salary_from, salary_to, url, employer)
