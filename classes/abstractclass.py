from abc import ABC, abstractmethod


class GetVacancies(ABC):
    @abstractmethod
    def get_vacancies(self, name, keyword, salary):
        pass

