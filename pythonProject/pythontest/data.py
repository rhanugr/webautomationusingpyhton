import pytest

class Data:

    def __init__(self,driver):
        self.driver = driver

    @pytest.fixture(params=[{"firstname":"hanamanta"}])
    def getData(self,request):
        return request.params
