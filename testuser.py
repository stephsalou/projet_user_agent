import requests
import json
try :
    req = requests.get(url='http://localhost:8000/test/')
    if req.status_code == 200:
        result = json.loads(req.text)
        print(result)
    else:
        print('fail')
    print(req.status_code)
except :
    print('request error')