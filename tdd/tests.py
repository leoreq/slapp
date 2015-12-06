from django.test import TestCase
#Core resolvers are the ones that will process the User URL request.
from django.core.urlresolvers import resolve
from tdd.views import pag_inicio
from django.http import HttpRequest
from django.template.loader import render_to_string
from tdd.models import Item

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

    def test_pagina_inicio_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = pag_inicio(request)

        self.assertEqual(Item.objects.count(),1)
        new_item=Item.objects.first()
        self.assertEqual(new_item.text,'A new list item')

        #self.assertIn('A new list item', response.content.decode())
    def test_pagina_inicio_can_redirect_after_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = pag_inicio(request)

        self.assertEqual(response.status_code,302)
        self.assertEqual(response['location'],'tdd/pag_inicio/')

    def test_pagina_inicio_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        request = HttpRequest()
        response = pag_inicio(request)

        self.assertIn('itemey 1',response.content.decode())
        self.assertIn('itemey 2',response.content.decode())

    def test_pagina_inicio_saves_only_when_needed(self):
        request=HttpRequest()
        response=pag_inicio(request)
        self.assertEqual(Item.objects.count(),0)

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')
