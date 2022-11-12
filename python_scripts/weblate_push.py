import requests
import json

url = "http://40.76.85.234/api/translations/test/readme-example/ko/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

result = json.loads(response.text)
print(result["translated_percent"])

if result["translated_percent"]>=3:
    
    url = "http://40.76.85.234/api/translations/test/readme-example/ko/repository/"

    payload = json.dumps({
    "operation": "push"
    })
    headers = {
    'Authorization': 'Bearer wlu_oY6KhWRDjIpLWPuoYZMD4IL3fU2lmHEvCuvw',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
