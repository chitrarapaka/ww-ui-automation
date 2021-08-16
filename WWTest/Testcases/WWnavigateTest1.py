from selenium import webdriver
from Pages.Findstudiopage import Findstudiopage
from Pages.Businesshourspage import Businesshours
import logging


# Set the chromedriver path and change the below path to local chromedriver path
chrome_path = r'/Users/chitrarapaka/PycharmProjects/pythonProject/venv/bin/chromedriver 2'
driver = webdriver.Chrome(executable_path=chrome_path)
base_url=("https://www.weightwatchers.com/us/find-a-workshop/")
try:
    logging.basicConfig(filename="WWTestCaseLog.txt",format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

except:

    print("Not able to write logs.Permissions might be wrong")

def set_up():
    driver.maximize_window()
    driver.get(base_url)
    driver.implicitly_wait(10)


def test_findstudio():
    fs = Findstudiopage(driver)
    fs.test_title(logger)
    fs.click_studio(logger)
    fs.search_address(logger)
    title_return = fs.searchresult(logger) # Return the first search result title and store in title_return as next statement will navigate to businesshours page
    fs.clickfirstlink(logger)
    return (title_return)


def test_businesshours(search_title):
    bh = Businesshours(driver)
    bh.compare_title(search_title)
    bh.click_businesshours(logger)
    bh.print_businesshours(logger)
    bh.quit_chrome()


#Main program to trigger the testcase
set_up()
searchresult = test_findstudio()
test_businesshours(searchresult)

