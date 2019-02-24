from selenium import webdriver
import time

class Gmail_Driver():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'/usr/bin/safaridriver')


    def signup(self, first_name, last_name, username, password):
        self.driver.get('https://accounts.google.com/signup/v2/webcreateaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F%3Fpc%3Dtopnav-about-en&flowName=GlifWebSignIn&flowEntry=SignUp')
        self.driver.find_element_by_id('firstName').send_keys(first_name)
        self.driver.find_element_by_id('lastName').send_keys(last_name)
        self.driver.find_element_by_id('username').send_keys(username)
        self.driver.find_element_by_name('Passwd').send_keys(password)
        self.driver.find_element_by_name('ConfirmPasswd').send_keys(password)
        self.driver.find_element_by_id('accountDetailsNext').click()

    def signin(self, username, password):
        self.driver.get('https://www.gmail.com')
        self.driver.find_element_by_id('identifierId').send_keys(username)
        self.driver.find_element_by_id('identifierNext').click()
        time.sleep(2)
        self.driver.find_element_by_class_name('whsOnd.zHQkBf').send_keys(password)
        self.driver.find_element_by_id('passwordNext').click()

gmail = Gmail_Driver()
gmail.signup('Shreya', 'Dudu', 'shreya.dudu', 'duduuuuu')