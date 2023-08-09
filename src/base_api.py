import json
from abc import ABC, abstractmethod


class Api(ABC):
    def __init__(self) -> None:
        self.response = list()
        self.file = None

    @abstractmethod
    def get_vacancies(self, serch_query):
        pass

    def write_json(self) -> None:
        with open(self.file, "w", encoding='utf-8') as file:
            json.dump(self.response, file, ensure_ascii=False, indent=2)
