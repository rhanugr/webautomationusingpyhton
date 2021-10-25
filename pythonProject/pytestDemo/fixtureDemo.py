import pytest


@pytest.mark.usefixtures("setup")
class TestSetup:

    def test_cal1(self):
        print("Demo1")

    def test_cal2(self):
        print("Demo2")

    def test_cal3(self):
        print("Demo3")
