class QualityAssurancePage():
    def __init__(self, driver, By , WebDriverWait, EC):
        self.driver = driver
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.By = By
        self.seeAllQaJobs = "//a[text()='See all QA jobs']"

    def clickSeeAllQaJobs(self):
        self.WebDriverWait(self.driver, 30).until(self.EC.visibility_of_element_located(
            (self.By.XPATH, self.seeAllQaJobs)))
        self.driver.execute_script("arguments[0].scrollIntoView();",
                                   self.driver.find_element(self.By.XPATH, self.seeAllQaJobs))
        self.driver.execute_script("arguments[0].click();", self.driver.find_element(self.By.XPATH, self.seeAllQaJobs))
