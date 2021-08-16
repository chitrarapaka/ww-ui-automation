from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver



class Businesshours:

    def __init__(self, drv):
        self.drv = drv
        self.drv.implicitly_wait(10)

# Step 7 : Verify if location title/name matches with the search result clicked on step 5

    def compare_title(self,search_title):
        title2 = self.drv.find_element_by_xpath("//div[@class = 'infoContainer-12kv1']/h1").text
        if title2 == search_title:
            print("current title matches with first search result")
        else:
            print("not matching")

# Step 8 : Click-Business hours-expand the down arrow

    def click_businesshours(self, logger):
        self.drv.find_element_by_css_selector("svg[class = 'hoursIcon-II-H2']").click()
        logger.info("step8_clickbusinesshours")
        self.drv.save_screenshot('step8_searchresult.png')

# Step9 : Prints business hours,as well as output is stored to the text file

    def print_businesshours(self,logger):
        bh_list = []
        output = self.drv.find_element_by_xpath("//div[@class = 'hoursWrapper-1KHIv show-1db4o']")
        b_hours = output.text
        bh_list = b_hours.split("\n")
        textfile = open("bh_output.txt","w")
        for element in bh_list:
            if not element.endswith("day"):
                textfile.write(element)
                print(element+'\n')
                textfile.write('\n')
            else:
                element = element + ' '
                textfile.write(element)
                print(element)
        textfile.close()
        logger.info("step9_print_businesshours")


    def quit_chrome(self):
        self.drv.quit()
