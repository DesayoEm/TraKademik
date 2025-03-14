import os
from pathlib import Path
from dotenv import load_dotenv

app_dir = Path(__file__).resolve().parent.parent / 'app'
env_path = app_dir / '.env'

load_dotenv(dotenv_path=env_path)

TEST_DB_URL = os.getenv('TEST_DB_URL')
TEST_DB_PWD = os.getenv('TEST_DB_PWD')

