import requests
from requests.auth import HTTPBasicAuth

def test_auth():
    url ="https://api.github.com/user"
    response = requests.get(url,auth=HTTPBasicAuth('hanamanta','Test'))
    print(response.text)