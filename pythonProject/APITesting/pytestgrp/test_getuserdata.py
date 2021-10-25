import pytest
import requests
import json
import jsonpath


@pytest.mark.Smoke
def test_fetch_user_data():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    json_response = json.loads(response.text)
    # print(json_response)
    for i in range(0,6):
        first_name = jsonpath.jsonpath(json_response,'data['+str(i)+'].first_name')
        last_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].last_name')
        print(first_name[0] + " " +last_name[0])
        # print(last_name[0])

