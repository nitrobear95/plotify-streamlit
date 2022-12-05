
from app import test_input1
import requests

def get_api():
    url = "https://gpt-summarization.p.rapidapi.com/summarize"

    payload = {
        "text": input1,
        "num_sentences": 3}

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "1688bcf98dmsh0dde3eda4f0374ap15d984jsnbb0c2deccb48",
        "X-RapidAPI-Host": "gpt-summarization.p.rapidapi.com"
        }

    response = requests.request("POST", url, json=payload, headers=headers)

    return response.text
