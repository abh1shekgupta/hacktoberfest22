import os
import pytest
from selenium import webdriver

@pytest.fixture(params=["chrome"], scope="function")
def driver(request):
    # invoke driver object
    global web_driver
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    elif request.param == "chrome":
        web_driver = webdriver.Chrome()
    def teardown():
        print('Function Tear down - - - - ')
        web_driver.close()
    request.addfinalizer(teardown)

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    #"Define the HTML reporting stuff to generate the HTML"
    pass

def _capture_screenshot(name):
    # Write screenshot method

@pytest.fixture(scope="class")
def test_data(request):
    # define static data or load any external file
    request = "testdata1"
    pass