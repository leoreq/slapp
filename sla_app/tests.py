from django.test import TestCase,Client
#Core resolvers are the ones that will process the User URL request.
from django.core.urlresolvers import resolve
from sla_app.views import home,pag_inicio,profile_update,create_service_contract,view_list,delete_item
from django.http import HttpRequest
from django.template.loader import render_to_string
from sla_app.models import Company, List, Item
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
# Create your tests here.


class HomePageTest(TestCase):

    def test_root_urlresolve_to_homepage_view(self):
        found=resolve('/slapp/')

        self.assertEqual(found.func,home)

    def test_page_returns_correct_html(self):
        request=HttpRequest()
        response=home(request)

        expected_html=render_to_string('sla_app/home.html')

        self.assertEqual(response.content.decode(),expected_html)

class CompanyProfileUpdateTest(TestCase):
    def setUp(self):
        test_user=User.objects.create_user(username="test_user",password="testpass")
        self.c=self.client
        self.c.login(username="test_user",password="testpass")

    def test_page_urlresolve_to_profile_update_view(self):
        found=resolve('/slapp/profile_update/')

        self.assertEqual(found.func,profile_update)

    def test_uses_a_profile_update_template(self):
        response=self.client.get('/slapp/profile_update/')
        self.assertTemplateUsed(response,'sla_app/profile_update.html')

    def test_profile_update_can_save_a_POST_request(self):

        response=self.client.post('/slapp/profile_update/', 
            {'name':'New Testing Corp',
            'service': 'New Testing Services'})
                
        self.assertEqual(Company.objects.count(),1)
        new_company=Company.objects.first()
        self.assertEqual(new_company.name,'New Testing Corp')
        self.assertEqual(new_company.service,'New Testing Services')


    def test_profile_update_can_redirect_after_POST_request(self):

        response = self.client.post('/slapp/profile_update/', 
            {'name':'New Testing Corp',
            'service': 'New Testing Services'})
        new_company=Company.objects.first()
        #self.assertEqual(response.status_code,302)
        #self.assertEqual(response['location'],'/slapp/profile_update/')
        self.assertRedirects(response,'/slapp/company/%d/'%new_company.user.id)

    def test_profile_info_ca_be_rendered_after_redirect(self):
        response = self.client.post('/slapp/profile_update/', 
            {'name':'New Testing Corp',
            'service': 'New Testing Services'})
        new_company=Company.objects.first()
        
        response2=self.client.get('/slapp/company/%d/'%new_company.user.id)
        
        self.assertContains(response2,new_company.name)
        self.assertContains(response2,new_company.service)

class CompanyProfileViewTest(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username="test_user",password="testpass")
        self.c=self.client
        self.c.login(username="test_user",password="testpass")
    
    def test_correct_profile_info_is_rendered_after_redirect(self):
        test_user=User.objects.get(username="test_user")
        new_company=Company.objects.create(user=test_user,name='New Testing Corp',service='This is a company that tests things')
        
        response=self.client.get('/slapp/company/%d/'%new_company.user.id)
        
        self.assertContains(response,new_company.name)
        self.assertContains(response,new_company.service)

    def test_uses_a_CompanyProfile_template(self):
        test_user=User.objects.get(username="test_user")
        new_company=Company.objects.create(user=test_user,name='New Testing Corp',service='This is a company that tests things')
          
        response=self.client.get('/slapp/company/%d/'%new_company.user.id)
        self.assertTemplateUsed(response,'sla_app/company_profile.html')

class ServiceContractCreateViewTest(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username="test_user",password="testpass")
        self.c=self.client
        self.c.login(username="test_user",password="testpass")
        new_company=Company.objects.create(user=self.test_user,name='New Testing Corp',service='This is a company that tests things')

    def test_page_urlresolve_to_profile_update_view(self):
        new_company=Company.objects.get(name='New Testing Corp')
        
        found=resolve('/slapp/company/%d/service_contract/'%new_company.user.id)

        self.assertEqual(found.func,create_service_contract)

    def test_service_contract_urlresolve_to_profile_update_view(self):
        new_company=Company.objects.get(name='New Testing Corp')

        response=self.client.get('/slapp/company/%d/service_contract/'%new_company.user.id)

        self.assertTemplateUsed(response,'sla_app/create_service_contract.html')

class CompanyModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_user=User.objects.create_user('testuser1','test@gmail.com',password='testpass')

        first_company = Company()
        first_company.user=first_user
        first_company.name = 'New Testing Corp'
        first_company.service='This is a company that tests things'
        first_company.save()

        second_user=User.objects.create_user('testuser2','test2@gmail.com',password='testpass2')

        second_company = Company()
        second_company.user=second_user
        second_company.name = 'Old Testing Corp'
        second_company.service='This is a company that should tests things'
        second_company.save()

        saved_items = Company.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[1]
        second_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.name, 'New Testing Corp')
        self.assertEqual(second_saved_item.service, 'This is a company that should tests things')

class ListViewTest(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username="test_user",password="testpass")
        self.c=self.client
        self.c.login(username="test_user",password="testpass")
        new_company=Company.objects.create(user=self.test_user,name='New Testing Corp',service='This is a company that tests things')

    def test_page_urlresolve_to_listView_view(self):
        new_company=Company.objects.get(name='New Testing Corp')
        list_=List.objects.create(company=new_company)

        found=resolve('/slapp/company/%d/service_contract/%d/'%(new_company.user.id,list_.id))

        self.assertEqual(found.func,view_list)

    def test_uses_a_list_template(self):
        new_company=Company.objects.get(name='New Testing Corp')
        list_=List.objects.create(company=new_company)

        response=self.client.get('/slapp/company/%d/service_contract/%d/'%(new_company.user.id,list_.id))
        
        self.assertTemplateUsed(response,'sla_app/create_service_contract.html')

    def test_displays_all_list_items(self):

        new_company=Company.objects.get(name='New Testing Corp')
        correct_list=List.objects.create(company=new_company)
        
        Item.objects.create(text='itemey 1',list=correct_list)
        Item.objects.create(text='itemey 2',list=correct_list)

        wrong_list=List.objects.create(company=new_company)
        Item.objects.create(text='itemeymal 1',list=wrong_list)
        Item.objects.create(text='itemeymal 2',list=wrong_list)

        response = self.client.get('/slapp/company/%d/service_contract/%d/'%(new_company.user.id,correct_list.id))

        self.assertContains(response,'itemey 1')
        self.assertContains(response,'itemey 2')

        self.assertNotContains(response,'itemeymal 1')
        self.assertNotContains(response,'itemeymal 2')

class NewListTest(TestCase):
    def setUp(self):
        self.test_user=User.objects.create_user(username="test_user",password="testpass")
        self.c=self.client
        self.c.login(username="test_user",password="testpass")
        new_company=Company.objects.create(user=self.test_user,name='New Testing Corp',service='This is a company that tests things')

    def test_save_a_POST_request(self):
        new_company=Company.objects.get(name='New Testing Corp')
        list_=List.objects.create(company=new_company)

        self.client.post('/slapp/company/%d/service_contract/%d/add_item'%(new_company.user.id,list_.id), data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

    def test_can_save_a_POST_request_to_an_existing_list(self):
        new_company=Company.objects.get(name='New Testing Corp')
        other_list=List.objects.create(company=new_company)
        correct_list=List.objects.create(company=new_company)

        response=self.client.post('/slapp/company/%d/service_contract/%d/add_item'%(new_company.user.id,correct_list.id), 
            data={'item_text':'A new item for an existing list'})

        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new item for an existing list')
        self.assertEqual(new_item.list,correct_list)

    def test_redirect_to_list_view(self):
        new_company=Company.objects.get(name='New Testing Corp')
        other_list=List.objects.create(company=new_company)
        correct_list=List.objects.create(company=new_company)

        response=self.client.post('/slapp/company/%d/service_contract/%d/add_item'%(new_company.user.id,correct_list.id), 
            data={'item_text':'A new item for an existing list'})

        self.assertRedirects(response,'/slapp/company/%d/service_contract/%d/'%(new_company.user.id,correct_list.id))

    def test_passes_correct_list_to_template(self):
        new_company=Company.objects.get(name='New Testing Corp')
        other_list=List.objects.create(company=new_company)
        correct_list=List.objects.create(company=new_company)

        response=self.client.get('/slapp/company/%d/service_contract/%d/'%(new_company.user.id,correct_list.id))

        self.assertEqual(response.context['list'],correct_list)

    def test_delete_item_from_list(self):
        new_company=Company.objects.get(name='New Testing Corp')
        correct_list=List.objects.create(company=new_company)
        
        Item.objects.create(text='itemey 1',list=correct_list)
        Item.objects.create(text='itemey 2',list=correct_list)
        Item.objects.create(text='itemey 3',list=correct_list)

        obj_count=Item.objects.filter(list=correct_list).count()
        self.assertEqual(obj_count,3)

        Item.objects.get(text='itemey 3',list=correct_list).delete()
        obj_count=Item.objects.filter(list=correct_list).count()
   
        self.assertEqual(obj_count,2)

    def test_delete_item_from_correct_list(self):
        new_company=Company.objects.get(name='New Testing Corp')
        correct_list=List.objects.create(company=new_company)
        
        Item.objects.create(text='itemey 1',list=correct_list)
        Item.objects.create(text='itemey 2',list=correct_list)
        Item.objects.create(text='itemey 3',list=correct_list)

        obj_count=Item.objects.filter(list=correct_list).count()
        self.assertEqual(obj_count,3)

        wrong_company=Company.objects.get(name='New Testing Corp')
        wrong_list=List.objects.create(company=wrong_company)
        
        Item.objects.create(text='itemey 1',list=wrong_list)
        Item.objects.create(text='itemey 2',list=wrong_list)
        Item.objects.create(text='itemey 3',list=wrong_list)

        obj_count=Item.objects.filter(list=wrong_list).count()
        self.assertEqual(obj_count,3)

        Item.objects.get(text='itemey 3',list=correct_list).delete()

        obj_count=Item.objects.filter(list=wrong_list).count()
   
        self.assertEqual(obj_count,3)

        obj_count=Item.objects.filter(list=correct_list).count()
   
        self.assertEqual(obj_count,2)

    def test_page_urlresolve_to_delete_item_view(self):
        new_company=Company.objects.get(name='New Testing Corp')
        list_=List.objects.create(company=new_company)
        item1=Item.objects.create(text='itemey 1',list=list_)

        found=resolve('/slapp/company/%d/service_contract/%d/delete/%d/'%(new_company.user.id,list_.id,item1.id))

        self.assertEqual(found.func,delete_item)

    def test_delete_item_from_delete_url(self):
        new_company=Company.objects.get(name='New Testing Corp')
        correct_list=List.objects.create(company=new_company)
        
        item1=Item.objects.create(text='itemey 1',list=correct_list)
        item2=Item.objects.create(text='itemey 2',list=correct_list)
        item3=Item.objects.create(text='itemey 3',list=correct_list)

        obj_count=Item.objects.filter(list=correct_list).count()
        self.assertEqual(obj_count,3)

        response=self.client.delete('/slapp/company/%d/service_contract/%d/delete/%d/'%(new_company.user.id,correct_list.id,item2.id))

        obj_count=Item.objects.filter(list=correct_list).count()
   
        self.assertEqual(obj_count,2)


