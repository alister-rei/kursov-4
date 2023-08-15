from abc import ABC, abstractmethod
from src.write_vacancy import JSONWriterMixin


class VacancyAPI(ABC, JSONWriterMixin):
    ''' Абстрактный класс для получения вакансий через Api '''
    vacancies_list = []

    @abstractmethod
    def get_vacancyes(self, town: str, keyword: str, count) -> list[dict[str]]:
        pass

    @abstractmethod
    def package_vacancyes(self, data_vacansyes: list[dict[str]]) -> None:
        pass
