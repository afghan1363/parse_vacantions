from abc import ABC, abstractmethod


class GetVacancies(ABC):
    @abstractmethod
    def get_vacancies(self, search_query, salary):
        pass

