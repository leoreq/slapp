from django.test import TestCase
#Core resolvers are the ones that will process the User URL request.
from django.core.urlresolvers import resolve
from tdd.views import pag_inicio
from django.http import HttpRequest
from django.template.loader import render_to_string
from tdd.models import Item, List

# Create your tests here.


class InicioPageTest(TestCase):

    def test_root_urlresolve_to_inicio_view(self):
        found=resolve('/tdd/pag_inicio/')

        self.assertEqual(found.func,pag_inicio)

    def test_page_returns_correct_html(self):
        request=HttpRequest()
        response=pag_inicio(request)

        expected_html=render_to_string('tdd/pagina_inicio.html')

        self.assertEqual(response.content.decode(),expected_html)


class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_=List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list=list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list=list_ 
        second_item.save()

        saved_list=List.objects.first()
        self.assertEqual(saved_list,list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list,list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list,list_)

class ListViewTest(TestCase):

    def test_uses_a_list_template(self):
        response=self.client.get('/tdd/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response,'tdd/list.html')

    def test_displays_all_list_items(self):
        list_=List.objects.create()
        Item.objects.create(text='itemey 1',list=list_)
        Item.objects.create(text='itemey 2',list=list_)

        response = self.client.get('/tdd/lists/the-only-list-in-the-world/')

        self.assertContains(response,'itemey 1')
        self.assertContains(response,'itemey 2')

class NewListTest(TestCase):
    def test_save_a_POST_request(self):
        self.client.post('/tdd/lists/new/', data={'item_text':'A new list item'})

        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

        #self.assertIn('A new list item', response.content.decode())
    def test_redirect_after_a_POST_request(self):
        response=self.client.post('/tdd/lists/new/', data={'item_text':'A new list item'})

        self.assertRedirects(response,'/tdd/lists/the-only-list-in-the-world/')
       