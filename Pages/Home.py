class HomePage():
    def __init__(self, driver, By , WebDriverWait, EC):
        self.driver = driver
        self.By = By
        self.WebDriverWait = WebDriverWait
        self.EC = EC
        self.more = "//a[./span[text()='More']]"
        self.careers = "//a[./h5[text()='Careers']]"
    def pageIsOpened(self):
        return self.driver.title

    def clickMore(self):
        self.WebDriverWait(self.driver, 20).until(self.EC.element_to_be_clickable(
            (self.driver.find_element(self.By.XPATH, self.more)))).click()

    def clickCareers(self):
        self.WebDriverWait(self.driver, 20).until(self.EC.element_to_be_clickable(
            (self.driver.find_element(self.By.XPATH, self.careers)))).click()

