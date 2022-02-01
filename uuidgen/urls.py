from django.contrib import admin
from django.urls import path
from core.views import uuid_gen
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', uuid_gen)
]
