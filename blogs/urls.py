from django.contrib import admin
from django.urls import path
from blogs.views import homeView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', homeView, name='index'),
]
