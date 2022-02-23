import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options as chrome_options


# @pytest.fixture
# def chrome_options(chrome_options):
#     options.headless = True
#     return chrome_options

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument("--headless")  # or '--headless' or 'chrome' for headless
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1400,1000')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(options=options)
    return driver


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # and pass this information to teardown:

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope='function')
def driver(get_webdriver, request):
    driver = get_webdriver
    driver.get("https://petfriends1.herokuapp.com/")
    yield driver
    if request.node.rep_call.passed:
        # Make the screen-shot if test failed:
        try:
            driver.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug:
            driver.save_screenshot('Screenshots/' + str(uuid.uuid4()) + '.png')  #  + str(uuid.uuid4()) +

            # For happy debugging:
            print('URL: ', driver.current_url)
            print('Browser logs:')
            for log in driver.get_log('browser'):
                print(log)

        except:
            pass  # just ignore any errors here
    driver.quit()
