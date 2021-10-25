import json
import jsonpath
import pytest
import requests

url = "https://reqres.in/api/users/2"
@pytest.fixture()
def start_exec():
    global file
    file = open("C:\Hanamanta_Data\Api Testing\putdata1.json", 'r')


@pytest.mark.Smoke
def test_user_create(start_exec):

    #Open the file in Read mode
    #Read the file usind file .read method
    json_input = file.read()
    #Parse to Json using Json.load method
    json_request =json.loads(json_input)
    #Send the request using PUT method(url, json_requests
    response = requests.put(url,json_request)
    #To print once Put method ran, use the content to print on console
    print(response.content)
    # To Read the data load into json response.text
    response_text = json.loads(response.text)
    # to Read the Content we should user JSON path
    name =jsonpath.jsonpath(response_text,'name')
    print(name[0])

@pytest.mark.Sanity
def test_user(start_exec):
    #Open the file in Read mode
    # file = open("C:\Hanamanta_Data\Api Testing\putdata1.json",'r')
    #Read the file usind file .read method
    json_input = file.read()
    #Parse to Json using Json.load method
    json_request =json.loads(json_input)
    #Send the request using PUT method(url, json_requests
    response = requests.put(url,json_request)
    #To print once Put method ran, use the content to print on console
    print(response.content)
    # To Read the data load into json response.text
    response_text = json.loads(response.text)
    # to Read the Content we should user JSON path
    name =jsonpath.jsonpath(response_text,'name')
    print(name[0])