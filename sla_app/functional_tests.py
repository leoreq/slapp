import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

##test if chrome webdriver is there
#driver = webdriver.Chrome('/Users/LeeX/Dropbox/Programming/Thinkfull/python/django/slapp/sla_app/chromedriver')  # Optional argument, if not specified will search path.
#driver.get('http://www.google.com/xhtml');
#time.sleep(5) # Let the user actually see something!
#search_box = driver.find_element_by_name('q')
#search_box.send_keys('ChromeDriver')
#search_box.submit()
#time.sleep(5) # Let the user actually see something!
#driver.quit()

class NewCompanyTest(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome('/Users/LeeX/Dropbox/Programming/Thinkfull/python/django/slapp/sla_app/chromedriver')  # Optional argument, if not specified will search path.

    def tearDown(self):
        self.browser.quit()

    def test_new_company_login(self):

        #Amibentes Proyectados company has heard about an app that will help them rate their provider work.

        #Juanito that works in the company decided to explore the webpage: /SLAPP
        self.browser.get('http://localhost:8000/slapp')
        ##self.browser.implicitely_wait(3)
        ##self.WebDriverWait(driver, 10)

        #Juanito is on the go so just is navigating the web page through his cell phone, and realizez that there is a nice welcoming page.
        
        #Juanito notices different elements on the page:
        # - SLAPP TITLE
        self.assertIn('SLAPP',self.browser.title) 
        header_text=self.browser.find_element_by_tag_name('h2').text
        self.assertIn('SLAPP',header_text)

        # - Three Buttons
        company_button_text=self.browser.find_element_by_id('companies_button').text
        self.assertIn('Companies',company_button_text)

        table = self.browser.find_elements_by_tag_name('button')
        self.assertTrue(
            any('EXPLORE'in row.text for row in table )
        )
        self.assertTrue( 
            any('MANAGE'in row.text for row in table )
        )
        self.assertTrue(
            any('EVALUATE'in row.text for row in table )
        )


        # - Footer

        #Juanito explores the page and enters the Company section
        self.browser.find_element(By.ID, "companies_button").click()
        WebDriverWait(self.browser, 10)

        login_form=self.browser.find_element_by_tag_name('form')

        inputs = self.browser.find_elements(By.XPATH, "//input")
        #While he clicks the page he gets prompted for a login. 
        inputbox = self.browser.find_element_by_id('login-username')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'username or email'
        )
        #As Juanito is new he will select to Sign up for a new account. 

        #Juanito enters the sign up page.
        
        self.browser.find_element(By.PARTIAL_LINK_TEXT,"Sign Up Here").click();
        login_form=self.browser.find_element_by_id('loginform')
        inputbox = self.browser.find_element_by_id('login-password2')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'confirm password'
        )
        #There he enters his login name.

        #Juanito mistakedly entered mismatching paswwords. 

        #Juanito then focuses and puts in matching passwords.

        #Juanito gets prompted to a new page that asks for more info
        self.fail('Finish the test')

if __name__=='__main__':
    unittest.main(warnings='ignore')

