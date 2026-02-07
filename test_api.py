import os

from dotenv import load_dotenv

load_dotenv()

api = os.getenv("RAPIDAPI_KEY")
print(api)

