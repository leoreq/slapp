
import time
from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
#from django.contrib.auth.models import User
#from .models import Company

class NewCompanyTest(TestCase):
    def setUp(self):
        self.browser=webdriver.Chrome('/Users/LeeX/Dropbox/Programming/Thinkfull/python/django/slapp/sla_app/chromedriver')  # Optional argument, if not specified will search path.
        # Before performing any tests, record the existing
        # user IDs:
        # 1. So we know which users we created during the test
        # 2. So we can remove just those fake users.
        #print ('setUp()')

        # Get the list of all users before the tests.
        # Must evaluate the QuerySet or it will be lazily-evaluated later, which is wrong.
        #self.users_before = list(User.objects.values_list('id', flat=True).order_by('id'))
        #print (self.users_before)

    def tearDown(self):
        self.browser.quit()
# #      print ('tearDown()')
 
 #      # Get the list of all users after the tests.
 #      users_after = list(User.objects.values_list('id', flat=True).order_by('id'))
 #      print (users_after)
 
 #      # Calculate the set difference.
 #      users_to_remove = sorted(list(set(users_after) - set(self.users_before)))
 #      print (users_to_remove)
 
 #      # Delete that difference from the database.
 #      User.objects.filter(id__in=users_to_remove).delete()

    def fill_element_id(self,element_id,placeholder,data_input):
        inputbox = self.browser.find_element_by_id(element_id)
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                placeholder
        )
        inputbox.send_keys(data_input)

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
        self.fill_element_id('login-username','username or email','testuser2')
        self.fill_element_id('login-password','password','testpasss')
        self.fill_element_id('login-password2','confirm password','testpasss')
        self.browser.find_element_by_id('registerbutton').click();
        import time
        time.sleep(3)
        #inputbox = self.browser.find_element_by_id('login-username')
        #self.assertEqual(
        #        inputbox.get_attribute('placeholder'),
        #        'username or email'
        #)
        #inputbox.send_keys('testuser')

        #Juanito mistakedly entered mismatching paswwords. 
        # Penging ...
        #Juanito then focuses and puts in matching passwords.
        #inputbox = self.browser.find_element_by_id('login-password')
        #self.assertEqual(
        #        inputbox.get_attribute('placeholder'),
        #        'password'
        #)
        #inputbox.send_keys('testpasss')
        #inputbox = self.browser.find_element_by_id('login-password2')
        #self.assertEqual(
        #        inputbox.get_attribute('placeholder'),
        #        'confirm password'
        #)
        #inputbox.send_keys('testpasss')
        
        
        inputbox.send_keys(Keys.ENTER)
        

        #Juanito gets prompted to a new page that asks for more info

        
        login_form=self.browser.find_element_by_id('profileupdateform')
        inputbox = self.browser.find_element_by_id('id_company_name')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter Company Name'
        )
        pass2inputbox.send_keys('New Testing Corp')
        pass2inputbox.send_keys(Keys.ENTER)


        #
        self.fail('Finish the test')

