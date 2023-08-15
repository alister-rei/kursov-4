from superjob_api import SJ_API
from headhunter_api import HH_API
from vacancy import Vacancy


def load_vacancy(choice:str|tuple, keyword:str, town:str, count:int) -> None:
    """
    Загружает вакансии с Api и записывает в файл
    :param choice: строка или кортеж для определения с каких платформ загружать вакансии
    :param keyword: Ключевое слово для поиска
    :param town: Город для поиска вакансий
    :param count: Количество вакансий запрашиваемых с сайта
    :return: None
    """
    if "hh" in choice:
        vacancy1 = HH_API()
        vacancyes = vacancy1.get_vacancyes(keyword, town, count)
        vacancy1.package_vacancyes(vacancyes)

    if "sj" in choice:
        vacancy2 = SJ_API()
        vacancyes = vacancy2.get_vacancyes(keyword, town, count)
        vacancy2.package_vacancyes(vacancyes)

    data = HH_API.vacancies_list
    HH_API.write_json(data)


def get_vacancyes() -> None:
    """
    Получение вакансий из файла и запись их в классы
    :return: None
    """
    vacancyes = Vacancy.read_vacancy()
    Vacancy.get_vacancy_from_list(vacancyes)


def print_vacancyes(mode) -> None:
    """
    Сортировка и вывод вакансий
    :param mode: режим сортировки вакансий
    :return: None
    """
    vacancyes = Vacancy.all_vacancy

    if mode == "2":
        Vacancy.sort_vacancy_from_date()
        vacancyes = Vacancy.all_vacancy
    elif mode == "3":
        vacancyes = sorted(Vacancy.all_vacancy)

    for vacancy in vacancyes:
        vacancy.print_vacancy()


