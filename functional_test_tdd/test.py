
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys




class ItemListTest(LiveServerTestCase):


    def setUp(self):
        self.browser=webdriver.Chrome('/Users/LeeX/Dropbox/Programming/Thinkfull/python/django/slapp/sla_app/chromedriver')  # Optional argument, if not specified will search path.


    def tearDown(self):
        self.browser.quit()
        print(self.live_server_url)


    def check_item_in_row(self,item_name):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(item_name,[row.text for row in rows])

    def fill_element_id(self,element_id,placeholder,data_input):
        inputbox = self.browser.find_element_by_id(element_id)
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                placeholder
        )
        inputbox.send_keys(data_input)
        inputbox.send_keys(Keys.ENTER)


    def test_can_start_a_list_and_retrieve_it_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        #self.browser.get('http://localhost:8000/tdd/pag_inicio')
        self.browser.get(self.live_server_url+'/tdd/pag_inicio')

        # She notices the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item straight away
        #inputbox = self.browser.find_element_by_id('id_new_item')
        #self.assertEqual(
        #        inputbox.get_attribute('placeholder'),
        #        'Enter a to-do item'
        #)
#
        ## She types "Buy peacock feathers" into a text box (Edith's hobby
        ## is tying fly-fishing lures)
        #inputbox.send_keys('Buy peacock feathers')
        #inputbox.send_keys(Keys.ENTER)
        
        self.fill_element_id('id_new_item','Enter a to-do item','Buy peacock feathers')
        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        #import time
        #time.sleep(10)




        self.check_item_in_row('1: Buy peacock feathers')
    

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        self.fill_element_id('id_new_item','Enter a to-do item','Use peacock feathers to make a fly')
       

        edith_list_url=self.browser.current_url
        self.assertRegex(edith_list_url,'/tdd/pag_inicio/lists/.+')


        # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')

        #table = self.browser.find_element(by=By.ID, value="id_list_table")
        rows = table.find_elements_by_tag_name('tr')
        self.check_item_in_row('1: Buy peacock feathers')
        self.check_item_in_row('2: Use peacock feathers to make a fly')
            
        # Now a new user, Francis, comes along to the site.

        ## We use a new browser session to make sure that no information
        ## of Edith's is coming through from cookies etc #1
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visits the home page.  There is no sign of Edith's
        # list
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts a new list by entering a new item. He
        # is less interesting than Edith...
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own unique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/tdd/pag_inicio/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy milk', page_text)

        # Satisfied, they both go back to sleep

        import time
        time.sleep(5)
        
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.

        # She visits that URL - her to-do list is still there.

        # Satisfied, she goes back to sleep
        self.fail('Finish the test!')


