# pytest file should start with test or end with test
# pytest method name should start with test
import pytest


def test_crossbrowser(crossBrowser):
    print(crossBrowser[1])
