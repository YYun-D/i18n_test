import requests
import json
import os

BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
url = "http://azuresdkweblate.eastus.cloudapp.azure.com/api/translations/test/readme-example/ko/"

response = requests.request("GET", url)

result = json.loads(response.text)
print(result["translated_percent"])

if result["translated_percent"]>=3:
    
    url = "http://azuresdkweblate.eastus.cloudapp.azure.com/api/translations/test/readme-example/ko/repository/"

    payload = json.dumps({ "operation": "push" })
    headers = {
    'Authorization': BEARER_TOKEN,
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
