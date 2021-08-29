from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.homepage, name="home")
]
