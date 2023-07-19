from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


from Base.base_element import BaseElement
from Helper.elementVariable import *
from Helper.properties import *

class Amazon(BaseElement):
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        BaseElement.__init__(self, self.driver)

    def goToWebsite(self,url):
        self.driver.get(url)
            
    def login(self,username,password):
        self.click(By.XPATH, ele_login_page()['login_btn'])
        self.dropdown
        self.type((By.ID, ele_login_page()['user']),username)
        self.type((By.ID, ele_login_page()['password']),password)