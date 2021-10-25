import requests


def test_dog():

    response = requests.get("https://dog.ceo/api/breeds/image/random")
    print(response.status_code)
    print(response.text)