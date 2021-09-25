from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('accounts/', include('accounts.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('admin/', admin.site.urls),
    path('', include('home.urls'), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Решение проблемы с выводом фоток из БД