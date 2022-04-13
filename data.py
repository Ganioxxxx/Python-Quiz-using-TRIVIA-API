from curses import ALL_MOUSE_EVENTS
from urllib import response
import requests

from question_model import Question

parameters = {

    "amount": 10,
    "type": "boolean",
    "difficulty": "medium",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
