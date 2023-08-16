import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()  # Загрузка переменных окружения из файла .env

# Чтение переменных окружения
SJ_API_KEY = os.getenv("SuperJob_Api_Key")

# URL для получения списка вакансий
SJ_URL = "https://api.superjob.ru/2.0/vacancies/"
HH_URL = "https://api.hh.ru/vacancies"

# Путь к корневой папке проэкта
ROOT = Path(__file__).resolve().parent

# Путь к папкам проэкта
SRC = Path(ROOT, "src")
VACANCIES_JSON = Path(ROOT, "vacancies.json")


