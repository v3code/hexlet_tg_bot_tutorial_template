import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['BOT_TOKEN']
DATABASE_URI = os.environ['DATABASE_URI']
IS_DEBUG = os.environ.get('IS_DEBUG', 'false').lower() == 'true'
