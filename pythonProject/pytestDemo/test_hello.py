# pytest file should start with test or end with test
# pytest method name should start with test
import pytest

@pytest.mark.skip
def test_hello():
    print("Hello Panda")


@pytest.mark.xfail
def test_come():
    print("XPASS-----Due to Skipped and Returned the Result")
    
