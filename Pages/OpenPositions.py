import time


class OpenPositionsPage():
    def __init__(self, driver, By , WebDriverWait, EC, Select):
        self.driver = driver
        self.By = By
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.Select = Select
        self.jobListID = "jobs-list"
        self.selectLocationID = "filter-by-location"
        self.selectLocationText = "Istanbul, Turkey"
        self.selectDepartmentID = "filter-by-department"
        self.selectDepartmentText = "Quality Assurance"
        self.applyNow = "//div[@data-location='istanbul-turkey' and @data-team='qualityassurance']/div/a"
        self.positionTitles = "(//p[contains(@class,'position-title')])"
        self.expectPositionTitles = "Quality Assurance"
        self.expectPositionTitles2 = "QA"
        self.positionDepartments = "(//span[contains(@class,'position-department')])"
        self.expectPositionDepartment = "Quality Assurance"
        self.positionLocations = "(//div[contains(@class,'position-location')])"
        self.expectPositionLocation = "Istanbul, Turkey"
        self.applyNowButtons = "(//a[text()='Apply Now'])"
        self.leverLinkText = "jobs.lever.co"


    def isJobsListExist(self):
        try:
            self.driver.find_element(self.By.ID, self.jobListID)
        except:
            return False
        return True

    #expectPositionTitles2 has been added so that the rest of the test can be seen.
    def isPositionVariablesExist(self):
        self.WebDriverWait(self.driver, 30).until(self.EC.visibility_of_element_located(
            (self.By.XPATH, self.positionTitles)))
        time.sleep(1)
        for x in range(1, 5):
            positionTitle = self.driver.find_element(self.By.XPATH, self.positionTitles + '[' + str(x) + ']')
            positionDepartment = self.driver.find_element(self.By.XPATH, self.positionDepartments + '[' + str(x) + ']')
            positionLocation = self.driver.find_element(self.By.XPATH, self.positionLocations + '[' + str(x) + ']')
            if self.expectPositionTitles not in positionTitle.text and self.expectPositionTitles2 not in positionTitle.text:
                print(positionTitle.text)
                return False
            if self.expectPositionDepartment not in positionDepartment.text:
                print(positionDepartment.text)
                return False
            if self.expectPositionLocation not in positionLocation.text:
                print(positionLocation.text)
                return False
            try:
                self.driver.find_element(self.By.XPATH,  self.applyNowButtons + '[' + str(x) + ']')
            except:
                return False

        return True


    def filterJobs(self):
        self.WebDriverWait(self.driver, 30).until(self.EC.visibility_of_element_located(
            (self.By.ID, self.selectLocationID)))
        self.Select(self.driver.find_element(self.By.ID,self.selectLocationID)).select_by_visible_text(self.selectLocationText)
        self.Select(self.driver.find_element(self.By.ID, self.selectDepartmentID)).select_by_visible_text(self.selectDepartmentText)

    def checkApplyNowLink(self):
        self.WebDriverWait(self.driver, 30).until(self.EC.presence_of_element_located(
            (self.By.XPATH, self.applyNow)))
        if self.leverLinkText not in self.driver.find_element(self.By.XPATH, self.applyNow).get_attribute('href'):
            return False
        return True


    def clickApplyNow(self):
        self.WebDriverWait(self.driver, 30).until(self.EC.presence_of_element_located(
            (self.By.XPATH, self.applyNow)))
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(self.By.XPATH, self.applyNow))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(self.By.XPATH, self.applyNow))
