
import json
import jsonpath
import requests

def test_add_new_student():
    global id
    url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Hanamanta_Data/Api Testing/addstudent.json",'r')
    json_req =json.loads(file.read())
    response = requests.post(url,json_req)
    id = jsonpath.jsonpath(response.json(),'id')
    print(id[0])
    print(response.text)

def test_get_details():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails/"+str(id[0])
    print(api_url)
    response = requests.get(api_url)
    print("======================================")
    print(response.text)






