class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ("title", "desc", "salary_from", "salary_to", "url", "employer")
    all_vacancies = []  # список полученных и отформатированных вакансий

    def __init__(self, title, desc, salary_from, salary_to, url, employer):
        self.title = title
        self.desc = desc
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.employer = employer
        Vacancy.all_vacancies.append({'title': self.title,
                                      'employer': self.employer,
                                      'description': self.desc,
                                      'salary_from': self.salary_from,
                                      'salary_to': self.salary_to,
                                      'url': self.url
                                      })

    def __str__(self) -> str:
        return (f"Название: {self.title},\nСсылка: {self.url},\nЗарплата: от {self.salary_from} до {self.salary_to}, "
                f"\nОписание: {self.desc}")

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__slots__})"

    def __lt__(self, other):
        return int(self.salary_from) < int(other.salary_from)

    def __le__(self, other):
        return int(self.salary_from) <= int(other.salary_from)

    def __gt__(self, other):
        return int(self.salary_from) > int(other.salary_from)

    def __ge__(self, other):
        return int(self.salary_from) >= int(other.salary_from)
