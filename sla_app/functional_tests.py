import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

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
            any('EXPLORE'in row.text for row in table ),
        )
        self.assertTrue( 
            any('MANAGE'in row.text for row in table ),
            "Company button is not appearing"
        )
        self.assertTrue(
            any('EVALUATE'in row.text for row in table ),
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

        #There he enters his login name.
        inputbox = self.browser.find_element_by_id('login-username')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'username or email'
        )
        inputbox.send_keys('testuser')
        inputbox.send_keys(Keys.ENTER)
        
        #import time
        #time.sleep(10)

        #Juanito mistakedly entered mismatching paswwords. 
        pass1inputbox = self.browser.find_element_by_id('login-password')
        self.assertEqual(
                pass1inputbox.get_attribute('placeholder'),
                'password'
        )
        pass1inputbox.send_keys('testpasss')
        pass1inputbox.send_keys(Keys.ENTER)
        pass2inputbox = self.browser.find_element_by_id('login-password2')
        self.assertEqual(
                pass2inputbox.get_attribute('placeholder'),
                'confirm password'
        )
        pass2inputbox.send_keys('mismatchingtestpasss')
        pass2inputbox.send_keys(Keys.ENTER)
        #Juanito then focuses and puts in matching passwords.

        #Juanito gets prompted to a new page that asks for more info
        self.fail('Finish the test')

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get('http://localhost:8000/pag_inicio')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)



        table = self.browser.find_element_by_id('id_list_table')

        #table = self.browser.find_element(by=By.ID, value="id_list_table")
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
    

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)


        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')

        #table = self.browser.find_element(by=By.ID, value="id_list_table")
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers',[row.text for row in rows])
        self.assertIn('2: Use peacock feathers to make a fly',[row.text for row in rows])
        #import time
        #time.sleep(2)
        
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
        self.fail('Finish the test!')


if __name__=='__main__':
    unittest.main(warnings='ignore')

