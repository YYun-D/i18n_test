import requests
import json
import os

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
WEBLATE_URL = "http://azuresdkweblate.eastus.cloudapp.azure.com/api/%s"

def read_translated_percent():
    url = WEBLATE_URL % "translations/test/readme-example/ko/"

    response = requests.request("GET", url)

    result = json.loads(response.text)
    return result["translated_percent"]

def push_repository_from_weblate():
    url =  WEBLATE_URL % "translations/test/readme-example/ko/repository/"

    payload = json.dumps({ "operation": "push" })
    headers = {
        'Authorization': BEARER_TOKEN, 
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.text

if __name__ == '__main__':
    if  read_translated_percent() >= 3:
        push_repository_from_weblate()
    
