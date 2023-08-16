from datetime import datetime
from settings import SJ_API_KEY, SJ_URL
from vacancy_api import VacancyAPI
from errors import ParsingError
import requests


class SJ_API(VacancyAPI):
    """ Класс для получения вакансий с Api hh.ru """

    @classmethod
    def get_vacancyes(cls, keyword: str, town: str, count) -> list[dict[str]]:
        """
        Получает вакансии с сайта в формате json словарей
        :param town: Город где искать вакансии
        :param keyword: Ключевое слово для поиска
        :param count: Количество вакансий по-умолчанию 10
        :return: список вокансий в формате json словарей
        """
        params = {
            "keyword": keyword,
            "town": "Москва" if town == "1" else "Санкт-Патербург",
            "count": count
        }
        # Отправка запроса на сервер для получения списка вакансий
        response = requests.get(SJ_URL, headers={"X-Api-App-Id": SJ_API_KEY}, params=params)

        try:
            # Проверка получения данных с сайта
            if response.status_code == 200:
                data = response.json()
                return data["objects"]
            else:
                # В случае ошибки запроса будет выведено сообщение
                raise ParsingError(response.status_code)
        except ParsingError as ex:
            print(f"Ошибка в запросе: {ex}")

    @classmethod
    def package_vacancyes(cls, data_vacansyes: list[dict[str]]) -> None:
        """
        получает список со всеми данными вакансий с Api
        и складывает в список родительского класса
        :param data_vacansyes: Список с данными вакансий
        :return: None
        """
        vacancies = []
        try:
            for vacancy in data_vacansyes:
                # Создание списка для записи шаблона данных профессии в файл
                sorted_vacancy = {
                    "id": vacancy['id'],
                    "profession": vacancy['profession'],
                    "date_published": datetime.fromtimestamp(vacancy["date_published"]).strftime("%Y-%m-%d %H:%M"),
                    "salary_from": vacancy['payment_from'],
                    "salary_to": vacancy['payment_to'],
                    "type_of_work": vacancy['type_of_work']['title'],
                    "experience": vacancy['experience']['title'],
                    "requirement": vacancy['candidat'],
                    "link": vacancy['link']
                }
                vacancies.append(sorted_vacancy)
        except TypeError as ex:
            print(f"Тип данных для записи шаблона не корректен : {ex}")
        # Добавление вакансий в список в родительском классе
        VacancyAPI.vacancies_list.extend(vacancies)
