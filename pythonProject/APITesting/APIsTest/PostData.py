import json

import jsonpath
import requests

url = "https://reqres.in/api/users"
file = open("C:\\Hanamanta_Data\\Api Testing\\postdata.json",'r')
json_input =file.read()
request_json = json.loads(json_input)
response = requests.post(url,request_json)
print(response.content)
print(response.status_code)
assert response.status_code == 201
print(response.headers)
json_res = json.loads(response.text)
id = jsonpath.jsonpath(json_res,'id')
print(id[0])





