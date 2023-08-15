import json
from settings import VACANCIES_JSON


class JSONWriterMixin:
    ''' Миксин класс для записи данных в файл по указапому пути '''

    @staticmethod
    def write_json(data) -> None:
        ''' Метод для записи данных в файл по указапому пути '''
        with open(VACANCIES_JSON, "w", encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
