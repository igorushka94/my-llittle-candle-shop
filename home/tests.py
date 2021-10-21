from datetime import date
from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
import unittest

from home.models import Category, Product
from .logic import generate_a_folder_name_for_Product


class SmokeTest(TestCase):
    """  Тут лписание теста """

    def test_bad_maths(self):
        """Тест: Неправильные математические расчеты"""
        self.assertEqual(1 + 2, 3)


class HomePageTest(TestCase):
    """  Тест домашней страницы """

    def test_can_save_a_POST_request(self):
        """ тест: можно сохранить post-запрос """
        # response = self.client.post(
        #     '/', 
        #     data = {
        #         'title': 'test title',
        #         'description': 'test description',
        #         'available': True,
        #         'image': 'test-image.jpg',
        #         'price': 1000
        #         }
        #     )
        first_item = Item()
        first_item.title = 'test title'
        first_item.description = 'test description'
        first_item.available = True
        first_item.image = 'test-image.jpg'
        first_item.price = 1000
        
        new_item = Product.objects.last()
        self.assertEqual(new_item.title, 'test title')
        self.assertEqual(new_item.description, 'test description')
        self.assertTrue(new_item.available)
        self.assertEqual(new_item.image, 'test-image.jpg')
        self.assertEqual(new_item.price, 1000)


class logicTest(TestCase):

    product = Product(category=Category.objects.get(id=1), title='test title', description='test description', available=True, image='test_image.jpg', price=500)

    def test_generate_a_folder_name_for_Product(self):
        self.assertEqual(generate_a_folder_name_for_Product(isinstance=self.product, filename=self.product.image), r'F:\DJANGO\project\webcandlshop\media\candles\test_image.jpg')
        


if __name__ == "__main__":
    unittest.main()
