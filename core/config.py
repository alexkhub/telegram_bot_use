from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
DB_LINK = os.getenv('DB_LINK')