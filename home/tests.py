# from os import name
# from django.test import TestCase
# from django.urls import resolve
# from django.http import HttpRequest
# import unittest


# from views import index



# class SmokeTest(TestCase):
#     """  Тут лписание теста """

#     def test_bad_maths(self):
#         """Тест: Неправильные математические расчеты"""
#         self.assertEqual(1 + 2, 3)


# class HomePageTest(TestCase):
#     """  Тест домашней страницы """
#     def test_root_url_resolves_to_home_page_views(self):
#         """ Тест: корневой url преобразуется в представление домашней страницы """
#         found = resolve('/')
#         self.assertEqual(found.func, index)

#     # def test_home_page_returns_correct_html(self):
#     #     """  Тест: домашняя страница возвращает правильный html """
#     #     request = HttpRequest
#     #     response = index(request)
#     #     self.assertTrue(response)
#     #     self.assertIn('<title>Интернет-магазин</title>')
#     #     self.assertTrue(html.endswith('</html>'))


# if __name__ == "__main__":
#     unittest.main()