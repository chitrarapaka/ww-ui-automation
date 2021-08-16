from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
import logging





class Findstudiopage:
    title = 'Find WW Studios & Meetings Near You | WW USA'
    # matchtitle = re.search("^You | WW USA$", title)
    studio_icon_text = "studioIcon-2TdMR"
    address = "location-search"
    #studio_class_name = "buttonText-3DCCO"


    def __init__(self, drv):
        self.drv = drv
        self.drv.implicitly_wait(10)

    #Step2 :  Assert loaded page title contains “Find WW Studios & Meetings Near You | WW USA”

    def test_title(self, logger):
        print(self.title)
        print(self.drv.title)
        assert self.title.find(self.drv.title)
        logger.info("Asserted the Title Page Name match_step2")
        self.drv.save_screenshot('Assert_Title_step2.png')

    #Step 3 : Under Find workshops-Click on Studio

    def click_studio(self,logger):
        self.drv.find_element_by_class_name(self.studio_icon_text).click()
        logger.info("step3_clicked studio")
        self.drv.save_screenshot('step3_click_studio.png')

    #Step 4 : In search field, search for meetings with zip code - 10011

    def search_address(self,logger):
        #self.wait_variable.until(E.presence_of_element_located((By.ID, "location-search"))).click()
        self.drv.find_element_by_id('location-search').click()
        self.drv.find_element_by_id('location-search').send_keys('10011')
        #self.wait_variable.until(E.presence_of_element_located((By.CLASS_NAME, "rightArrow-daPRP'"))).click()
        self.drv.find_element_by_id('location-search-cta').click()
        logger.info("step4_search_address")
        self.drv.save_screenshot('step4_search_address.png')

# Step 5 : Print title of first search result and distance located
    def searchresult(self,logger):
        title = self.drv.find_element_by_xpath("//div[@class='results-aiUr3']/div[1]/a/div[1]/div[1]/a").text
        distance = self.drv.find_element_by_xpath("//div[@class='results-aiUr3']/div[1]/a/div[1]/span").text
        print(title, distance)
        logger.info("step5_searchresult")
        self.drv.save_screenshot('step5_searchresult.png')
        return (title)

#Step 6 : Click on first search result

    def clickfirstlink(self,logger):
        self.drv.find_element_by_xpath("//div[@class='results-aiUr3']/div[1]/a").click()
        logger.info("step6_clickfirstlink_")
        self.drv.save_screenshot('step6_clickfirstlink.png')