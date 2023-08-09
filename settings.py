import os
from pathlib import Path
from dotenv import load_dotenv


load_dotenv()  # Загрузка переменных окружения из файла .env

# Чтение переменных окружения
superjob_api_key = os.getenv("SuperJob_Api_Key")

# Путь к корневой папке проэкта
ROOT = Path(__file__).resolve().parent

# Путь к папкам проэкта
SRC = Path(ROOT, "src")
VACANCIES_JSON = Path(ROOT, "vacancies_json")

# Путь к файлам
HH_FILE = Path(VACANCIES_JSON, "hh_data_file.json")
SJ_FILE = Path(VACANCIES_JSON, "sj_data_file.json")
