# API testing student management system
# 1.Add a new Student (POST)
# 2.Fetch student details(GET)
# 3.Update Student details(PUT)
# 4.Delete Student details(DELETE)
import pytest
import requests
import json
import jsonpath


#Post method used to add the data to the Server
# @pytest.mark.skip
def test_add_student_data():
    # API_URL = "http://www.thetestingworldapi.com/api/studentsDetails"
    # file_read =open("C:/Hanamanta_Data/Api Testing/sudent_details.json",'r')
    # json_load = json.loads(file_read.read())
    # response_api = requests.post(API_URL,json_load)
    # print(response_api.text)
    url = "http://www.thetestingworldapi.com/api/studentsDetails"
    # open the file in read mode
    file = open("C:/Hanamanta_Data/Api Testing/sudent_details.json",'r')
    # Load the json into Jsonformat file.read
    json_load = json.loads(file.read())
    # Now send the request
    response_add = requests.post(url,json_load)
    print(response_add.text)
    print(response_add.status_code)



#Use Get method : Used to fetch the data from the server
# @pytest.mark.skip
def test_get_student_data():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails/522442"
    response = requests.get(api_url)
    print(response.text)
    # json_res = json.loads(response.text)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id[0])
    assert id[0] == 522442  #522441

#Put method to update the student data
# @pytest.mark.skip
def test_update_student_data():
    url = "http://www.thetestingworldapi.com/api/studentsDetails/522386"
    file = open('C:/Hanamanta_Data/Api Testing/update3.json','r')
    json_read = json.loads(file.read())
    response = requests.put(url,json_read)
    print(response.text)

# @pytest.mark.skip
def test_delete_student():
    url = "http://www.thetestingworldapi.com/api/studentsDetails/522386"
    response = requests.delete(url)
    print(response.text)

# @pytest.mark.skip
def test_get_student_data_delete():
    api_url = "http://www.thetestingworldapi.com/api/studentsDetails/522386"
    response = requests.get(api_url)
    print(response.text)
    # json_res = json.loads(response.text)
    json_response = response.json()
    id = jsonpath.jsonpath(json_response,'data.id')
    print(id[0])
    assert id[0] == 522386