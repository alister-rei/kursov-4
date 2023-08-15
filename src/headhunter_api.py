from datetime import datetime
from settings import HH_URL
from src.errors import ParsingError
from vacancy_api import VacancyAPI
import requests


class HH_API(VacancyAPI):
    """ Класс для получения вакансий с Api superjob.ru """

    def get_vacancyes(self, keyword: str, town: str, count) -> list[dict[str]]:
        """
        Получает вакансии с сайта в формате json словарей
        :param town: Город где искать вакансии
        :param keyword: Ключевое слово для поиска
        :param count: Количество вакансий по-умолчанию 10
        :return: список вокансий в формате json словарей
        """
        params = {
            "text": keyword,
            "area": town,
            "per_page": count
        }
        response = requests.get(HH_URL, params=params)
        # Проверка наличия сведений по зарплате в случае отсутствия "По договоренности"
        try:
            if response.status_code == 200:
                data = response.json()
                return data['items']
            else:
                # В случае ошибки запроса будет выведено сообщение
                raise ParsingError(response.status_code)

        except ParsingError as ex:
            print(f"Ошибка в запросе код: {ex.key_error}")

    def package_vacancyes(self, data_vacansyes: list[dict[str]]) -> None:
        """
        получает список со всеми данными вакансий с Api
        и складывает в список родительского класса
        :param data_vacansyes: Список с данными вакансий
        :return: None
        """
        vacancyes = []

        for vacancy in data_vacansyes:
            # Создание списка для записи шаблона данных профессии в файл
            date = datetime.strptime(vacancy['published_at'], "%Y-%m-%dT%H:%M:%S%z").strftime("%Y-%m-%d %H:%M")
            salary_from = 0
            salary_to = 0
            if not vacancy['salary'] is None:
                if not vacancy['salary']['from'] is None:
                    salary_from = vacancy['salary']['from']
                if not vacancy['salary']['to'] is None:
                    salary_from = vacancy['salary']['to']

            sorted_vacancy = {
                "id": vacancy['id'],
                "profession": vacancy['name'],
                "date_published": date,
                "salary_from": salary_from,
                "salary_to": salary_to,
                "type_of_work": vacancy['employment']['name'],
                "experience": vacancy['experience']['name'],
                "requirement": vacancy['snippet']['requirement'],
                "link": vacancy['alternate_url']
            }
            vacancyes.append(sorted_vacancy)
        # Добавление вакансий в список в родительском классе
        VacancyAPI.vacancies_list.extend(vacancyes)