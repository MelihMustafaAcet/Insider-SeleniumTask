import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.Home import HomePage
from Pages.Careers import CareersPage
from Pages.QualityAssurance import QualityAssurancePage
from Pages.OpenPositions import OpenPositionsPage


class PageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.WebDriverWait = WebDriverWait
        cls.EC = EC
        cls.By = By
        cls.Select = Select
        cls.driver.get("https://useinsider.com/")
        cls.driver.maximize_window()

    def test_Insider(self):
        driver = self.driver
        WebDriverWait = self.WebDriverWait
        EC = self.EC
        Select = self.Select
        homePageTitle = "Insider personalization engine for seamless customer experiences"
        Home = HomePage(driver, By, WebDriverWait, EC)
        self.assertEqual(Home.pageIsOpened(), homePageTitle, "The page did not open.")
        Home.clickMore()
        Home.clickCareers()
        Careers = CareersPage(driver, By, WebDriverWait, EC)
        self.assertTrue(Careers.blocksOpenedOrNot(), "The blocks did not open.")
        Careers.clickAllTeams()
        Careers.clickQualityAssurance()
        QualityAssurance = QualityAssurancePage(driver, By, WebDriverWait, EC)
        QualityAssurance.clickSeeAllQaJobs()
        OpenPositions = OpenPositionsPage(driver, By, WebDriverWait, EC, Select)
        self.assertTrue(OpenPositions.isJobsListExist(), "Job list not exist.")
        OpenPositions.filterJobs()
        self.assertTrue(OpenPositions.isPositionVariablesExist(), "Something went wrong.")
        self.assertTrue(OpenPositions.checkApplyNowLink(), "Something went wrong.")
        OpenPositions.clickApplyNow()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()





