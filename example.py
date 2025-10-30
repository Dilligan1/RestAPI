import json
import os

import requests
from dotenv import load_dotenv

load_dotenv()

response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
print(os.getenv("STAGE"))
print(response.json()["insult"])