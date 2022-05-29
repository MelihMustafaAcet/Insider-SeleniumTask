class CareersPage():
    def __init__(self, driver, By , WebDriverWait, EC):
        self.driver = driver
        self.By = By
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.allTeams = "//a[contains(@class,'loadmore')]"
        self.qualityAssurance = "//a[./h3[text()='Quality Assurance']]"
        self.ourLocationsID = "career-our-location"
        self.teamsID = "career-find-our-calling"
        self.lifeAtInsider = "//h2[text()='Life at Insider']"

    def blocksOpenedOrNot(self):
        try:
            self.driver.find_element(self.By.ID, self.ourLocationsID)
            self.driver.find_element(self.By.ID, self.teamsID)
            self.driver.find_element(self.By.XPATH, self.lifeAtInsider)
        except:
            return False
        return True

    def clickAllTeams(self):
        self.WebDriverWait(self.driver, 30).until(self.EC.visibility_of_element_located(
            (self.By.XPATH, self.allTeams)))
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(self.By.XPATH, self.allTeams))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(self.By.XPATH, self.allTeams))

    def clickQualityAssurance(self):
        self.WebDriverWait(self.driver, 30).until(self.EC.visibility_of_element_located(
            (self.By.XPATH, self.qualityAssurance)))

        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(self.By.XPATH, self.qualityAssurance))
        self.driver.execute_script("arguments[0].click();",
                                   self.driver.find_element(self.By.XPATH, self.qualityAssurance))
