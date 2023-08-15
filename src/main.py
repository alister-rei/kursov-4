from utils import load_vacancy, get_vacancyes, print_vacancyes


# Функция для взаимодействия с пользователем
def user_interaction():
    while True:
        platform: str = input("Выберите платформу для получения вакансий\n 1.HeadHunter 2.SuperJob 3.обе платформы : ")
        if platform not in ["1", "2", "3"]:
            print("Нет такой платформы попробуйте сначала")
            continue
        keyword: str = input("Введите ключевое слово для поиска вакансий : ")
        if len(keyword) < 3:
            print("Ключевое слово для поиска меньше 3-ч букв попробуйте сначала")
            continue
        print("Города, для которых можно получить вакансии: 1.Москва 2.Санкт-Патербург")
        town: str = input("Введите номер города : ")
        if town not in ["1", "2"]:
            print("Нет такого города попробуйте сначала")
            continue
        print("Количество вакансий, которые нужно получить по-умолчанию 10 для каждой платформы(целое число)")
        count = input("Введите число вакансий или нажмите Enter : ")
        count = int(count) if count else 10
        if not 0 <= count <= 100:
            print("Количество вакансий должно быть целым числом больше 0")
            continue

        # Получение параметров для разных платформ
        if platform == "1":
            load_vacancy("hh", keyword, town, count)
        elif platform == "2":
            load_vacancy("sj", keyword, town, count)
        elif platform == "3":
            load_vacancy(("hh", "sj"), keyword, town, count)

        print("Вакансии записаны в файл")
        # Загрузка вакансий в экземпляры класса из файла
        get_vacancyes()

        while True:
            print('''
            Для вывода вакансий в случайном порядке введите 1
            Для сортировки и вывода вакансий по дате введите 2
            Для сортировки и вывода вакансий по зарплате введите 3
            Для выхода введите 0
                        ''')
            mode: str = input("Введите режим вывода вакансий : ")
            if mode in ["1", "2", "3"]:
                print_vacancyes(mode)
            elif mode == "0":
                break
            else:
                print("Нет такого режима")
        break


if __name__ == "__main__":
    user_interaction()
