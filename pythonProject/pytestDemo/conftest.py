import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will Execute First TOP most")
    yield
    print("I am last Executor")


@pytest.fixture()
def dataLoad():
    print("User Data Loading from one master Method")
    return ["Prateek","Raghapur","Topuniversities"]

@pytest.fixture(params=[("Chrome","Prateek"),("FF","Prem"),("IE","3","1")])
def crossBrowser(request):
    return request.param
