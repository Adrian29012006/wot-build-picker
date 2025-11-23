from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('picker.urls')),  # все запросы на корень сайта отдаём в наше приложение
]
