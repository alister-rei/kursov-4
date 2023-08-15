import json
from json import JSONDecodeError
from settings import VACANCIES_JSON
from src.errors import MissingKeysException


class JSONReaderMixin:
    ''' mixin класс для чтения данных из файла с проверкой '''

    @staticmethod
    def read_vacancy() -> list[dict[str]]:
        '''
        метод для чтения данных из файла
        :param path: путь к фапйлу с данными
        :return: список словарей с данными
        '''
        keys = ["id", "profession", "date_published", "salary_from", "salary_to",
                "type_of_work", "experience", "requirement", "link"]
        try:
            with open(VACANCIES_JSON, "r", encoding='utf-8') as file:
                data = json.load(file)
                for vacancy in data:
                    missing_keys = [key for key in keys if key not in vacancy]
                    if missing_keys:
                        raise MissingKeysException(missing_keys)
                return data
        except FileNotFoundError as ex:
            print(f"Файл не найден\n {ex}")
        except MissingKeysException as ex:
            print(f"В файле нет ключа {ex.missing_keys}")
        except JSONDecodeError as ex:
            print(f"Файл поврежден {ex}")
