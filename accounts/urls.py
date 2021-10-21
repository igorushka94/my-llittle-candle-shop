from django.urls import path
from django.contrib.auth.views import LoginView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView

from . import views


app_name = 'accounts'
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name="logout"),
    path('profile/add_user_photo/', views.add_user_photo, name='add_user_photo'),
    path('profile/delete/', views.delete_photo_in_account, name='delete_photo_in_account'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]