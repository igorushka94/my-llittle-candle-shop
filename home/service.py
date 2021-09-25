# from django.contrib.auth.models import User
# from django.core.exceptions import MultipleObjectsReturned



# def searh_duplicate_email(email):
#     try:
#         User.objects.get(email=email)
#     except MultipleObjectsReturned:
#         return 'Пользователь с таким email уже существует! Введите другой email!'
#     except DoesNotExist:
#         return 'Уникальный email'
