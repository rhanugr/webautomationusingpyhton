import json
import jsonpath
import requests


def test_add_new_data():
    App_url = "http://www.thetestingworldapi.com/api/studentsDetails"
    file = open("C:/Hanamanta_Data/Api Testing/endtoend.json",'r')

    json_load = json.loads(file.read())
    response = requests.post(App_url,json_load)
    print(response.text)
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tec_url = "http://www.thetestingworldapi.com/api/technicalskills"
    file_tech = open("C:/Hanamanta_Data/Api Testing/techdetails1.json",'r')
    json_req = json.loads(file_tech.read())
    json_load['id'] = int(id[0])
    json_load['st_id'] = id[0]
    tech_response = requests.post(tec_url,json_req)
    print(tech_response.text)

    add_url = "http://www.thetestingworldapi.com/api/addresses"
    file_add = open("C:/Hanamanta_Data/Api Testing/add.json",'r')
    req_add = json.loads(file_add.read())
    json_load['stId'] = id[0]
    add_response =requests.post(add_url,req_add)


    final_details = "http://www.thetestingworldapi.com/api/FinalStudentDetails/522488"
    final_response = requests.get(final_details)
    print(final_response.text)







