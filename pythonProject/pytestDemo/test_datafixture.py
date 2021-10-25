import pytest


@pytest.mark.usefixtures("dataLoad")
class DataLoadTest:

    def test_data(self, dataLoad):
        print(dataLoad)