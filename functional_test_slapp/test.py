
from django.db import connection
from django.test.utils import setup_test_environment, teardown_test_environment

from slapp import settings
from sla_app.models import Company

from django.test import LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from django.contrib.auth.models import User


class NewCompanyTest(StaticLiveServerTestCase):
    def setUp(self):
        self.browser=webdriver.Chrome('/Users/LeeX/Dropbox/Programming/Thinkfull/python/django/slapp/sla_app/chromedriver')  # Optional argument, if not specified will search path.

    def tearDown(self):
        self.browser.quit()


    def fill_element_id(self,element_id,placeholder,data_input):
        inputbox = self.browser.find_element_by_id(element_id)
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                placeholder
        )
        inputbox.send_keys(data_input)

    def check_item_in_row(self,item_name):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(item_name,[row.text for row in rows])

    def check_item_not_in_row(self,item_name):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertNotIn(item_name,[row.text for row in rows])

    def test_new_company_login(self):

        #Amibentes Proyectados company has heard about an app that will help them rate their provider work.

        #Juanito that works in the company decided to explore the webpage: /SLAPP
        self.browser.get(self.live_server_url+'/slapp')

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

 
        #Juanito mistakedly entered mismatching paswwords. 
        # Penging ...
        #Juanito then focuses and puts in matching passwords.

        self.fill_element_id('login-password','password','testpasss')
        self.fill_element_id('login-password2','confirm password','testpasss')
        self.browser.find_element_by_id('registerbutton').click();
        
        #There he enters his login name.
        self.fill_element_id('login-username','username or email','testuser2')

 
        #Juanito mistakedly entered mismatching paswwords. 
        # Penging ...
        #Juanito then focuses and puts in matching passwords.

        self.fill_element_id('login-password','password','testpasss')
     
        self.browser.find_element_by_id('login_button').click();
                
        

        #Juanito gets prompted to a new page that asks for more info
        

        login_form=self.browser.find_element_by_id('profileupdateform')

        self.fill_element_id('id_company_name','Enter Company Name','New Testing Corp')
        self.fill_element_id('id_service','Enter detail of service ofered','New Testing Services')
        
        self.browser.find_element_by_id('updatebutton').click();

        #Juantito is redirected to the profile and can see all his updated information and some action buttons
        ## Company profile update page should be SLAPP/COMPANY/company_id/
        junaito_profile_url = self.browser.current_url
        self.assertRegex(junaito_profile_url , '/slapp/company/.+')
        
        #Create Service Contract Button
        ##Create service button will promt user to create a service, and add all the elements that it needs in order to fully replicate their sla".
    

        button = self.browser.find_element_by_id('create_service_contract_button').click()
        #
        ##Assuming that the session is logged in, URL: SLAPP/COMPANY/company_id/services/service_id
        junaito_profile_url = self.browser.current_url
        self.assertRegex(junaito_profile_url , '/slapp/company/.+/service_contract/')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Manage your contracts in a fly', page_text)
        self.assertIn('Add all the terms of your contract', page_text)
        
        self.fill_element_id('id_new_item','Eg .- Product Delivered on Time.','Deliver the testing suite in a timely manner')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)

        self.fill_element_id('id_new_item','Eg .- Product Delivered on Time.','Test , test and keep testing')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)
        self.fill_element_id('id_new_item','Eg .- Product Delivered on Time.','Conduct intensive testing suite')
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys(Keys.ENTER)

        self.check_item_in_row('1: Deliver the testing suite in a timely manner')
        self.check_item_in_row('2: Test , test and keep testing')
        self.check_item_in_row('3: Conduct intensive testing suite')

        #After adding a series of elements, the SAVE and GO BACK button redirects to the company profile page.
        self.browser.find_element_by_id('save_list_button').click()
        junaito_profile_url = self.browser.current_url

        self.assertRegex(junaito_profile_url , '/slapp/company/.+')
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertIn('Manage your contracts in a fly', page_text)
        self.assertNotIn('Add all the terms of your contract', page_text)
       
        #The details of the service have been saved, and a new Update Service Button appears. ***PENDING FOR Second Release
        #If you go back to the create service button You can see that the items that were previously saved are there.
        button = self.browser.find_element_by_id('create_service_contract_button').click()
        ##Assuming that the session is logged in, URL: SLAPP/COMPANY/company_id/services/service_id
        junaito_profile_url = self.browser.current_url
        self.assertRegex(junaito_profile_url , '/slapp/company/.+/service_contract/')
        page_text = self.browser.find_element_by_tag_name('body').text
        
        self.check_item_in_row('1: Deliver the testing suite in a timely manner')
        self.check_item_in_row('2: Test , test and keep testing')
        self.check_item_in_row('3: Conduct intensive testing suite')

        #You can delete an element by selecting the "x" span. 
        button = self.browser.find_element_by_id('2_contract_point_id_delete').click()

        self.check_item_in_row('1: Deliver the testing suite in a timely manner')
        self.check_item_not_in_row('2: Test , test and keep testing')
        self.check_item_in_row('2: Conduct intensive testing suite')

        #Once selected the created list, juanito can see his previously saved list and add new items to it.
        #He can also delete new items from it
        import time
        time.sleep(3)

        #CreateProvider Button
        ##This will update a list of providers,URL: SLAPP/COMPANY/company_id/providers/provider_id
        #Issue SLA Button

  


        #
        self.fail('Finish the test')

