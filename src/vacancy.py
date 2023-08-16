from datetime import datetime

from read_vacancy import JSONReaderMixin


class Vacancy(JSONReaderMixin):
    ''' Класс для хранения вакансий '''
    all_vacancy = []

    def __init__(self, __vacancy_id, __profession, __date_published, __salary_from,
                 __salary_to, __type_of_work, __experience, __requirement, __link) -> None:
        """
        Инициализация класса
        :param __vacancy_id: Id вакансии
        :param __profession: Название вакансии
        :param __date_published: Дата публикации
        :param __salary_from: Зарплата
        :param __salary_to: Зарплата
        :param __type_of_work: Тип работы
        :param __experience: Опыт работы
        :param __requirement: Описание вакансии
        :param __link: Ссылка на вакансию
        """
        self.__vacancy_id = __vacancy_id
        self.__profession = __profession
        self.__date_published = datetime.strptime(__date_published, "%Y-%m-%d %H:%M")
        self.__salary_from = __salary_from
        self.__salary_to = __salary_to
        self.__type_of_work = __type_of_work
        self.__experience = __experience
        self.__requirement = __requirement
        self.__link = __link

    @classmethod
    def get_vacancy_from_list(cls, data: list[dict[str]]) -> None:
        """
        Метод для создания экземпляров класса из списка данных
        :param data: список со словарями данных экземпляра
        :return: None
        """
        for vacancy in data:
            __vacancy_id = vacancy['id']  # Id вакансии
            __profession = vacancy['profession']  # Название вакансии
            __date_published = vacancy['date_published']  # Дата публикации
            __salary_from = vacancy['salary_from']  # Зарплата
            __salary_to = vacancy['salary_to']  # Зарплата
            __type_of_work = vacancy['type_of_work']  # Тип работы
            __experience = vacancy['experience']  # Опыт работы
            __requirement = vacancy['requirement']  # Описание вакансии
            __link = vacancy['link']  # Ссылка на вакансию
            cls_vacancy = cls(__vacancy_id, __profession, __date_published, __salary_from,
                              __salary_to, __type_of_work, __experience, __requirement, __link)
            # Сохранение экземпляра класса в список вакансий в классе
            cls.all_vacancy.append(cls_vacancy)

    @classmethod
    def sort_vacancy_from_date(cls) -> None:
        """ Сортирует вакансии по дате публикации """
        cls.all_vacancy = sorted(cls.all_vacancy, key=lambda x: x.__date_published)

    def __lt__(self, other):
        """ Метод для сортировки списка классов методом sorted по зарплате """
        if other.__class__.__name__ == self.__class__.__name__:
            return int(self.salary_from) < int(other.salary_from)
        else:
            print("Сравнивать можно только экземпляры класса Vacancy")

    def print_vacancy(self) -> None:
        """
        Выводит данные вакансии для пользователя
        вывод описания отключен
        :return: None
        """
        print(self.profession)
        print(self.date_published)
        print(self.type_of_work)
        print(f"{self.salary_from} - {self.salary_to}")
        print(self.experience)
        #print(self.requirement)
        print(self.link)

    @property
    def vacancy_id(self) -> str:
        """ Проперти для получения Id вакансии """
        return self.__vacancy_id

    @property
    def profession(self) -> str:
        """ Проперти для получения Название вакансии """
        return self.__profession

    @property
    def date_published(self) -> str:
        """ Проперти для получения Дата публикации """
        return self.__date_published.strftime("%Y-%m-%d %H:%M")

    @property
    def salary_from(self) -> str:
        """ Проперти для получения Зарплаты """
        return self.__salary_from

    @property
    def salary_to(self) -> str:
        """ Проперти для получения Зарплаты """
        return self.__salary_to

    @property
    def type_of_work(self) -> str:
        """ Проперти для получения Тип работы """
        return self.__type_of_work

    @property
    def experience(self) -> str:
        """ Проперти для получения Описание вакансии """
        return self.__experience

    @property
    def requirement(self) -> str:
        """ Проперти для получения Опыт работы """
        return self.__requirement

    @property
    def link(self) -> str:
        """ Проперти для получения Ссылка на вакансию """
        return self.__link
