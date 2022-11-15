import requests
import json
import os
import sys


BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
WEBLATE_URL = "http://azuresdkweblate.eastus.cloudapp.azure.com/api/%s"
PROJECT = sys.argv[1]
COMPONENT = sys.argv[2]
LANGUAGE = sys.argv[3]


def read_translated_percent():
    url = WEBLATE_URL % "translations/%s/%s/%s/" %(PROJECT, COMPONENT, LANGUAGE)
    
    response = requests.request("GET", url)

    result = json.loads(response.text)
    return result["translated_percent"]


def push_repository_from_weblate():
    url =  WEBLATE_URL % "translations/%s/%s/%s/repository/" %(PROJECT, COMPONENT, LANGUAGE)

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
    
