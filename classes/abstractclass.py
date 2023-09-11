from abc import ABC, abstractmethod


class GetVacancies(ABC):
    """
    Абстрактный класс для определения обязательного метода
    """
    @abstractmethod
    def get_vacancies(self):
        pass
