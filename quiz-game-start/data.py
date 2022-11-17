import requests
import json

response = \
    requests.get('https://opentdb.com/api.php?amount=15&category=15&difficulty=medium&type=boolean').text

question_data = json.loads(response)
results = question_data['results']