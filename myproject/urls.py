from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name="homepage"),
    path('accounts/', include('allauth.urls')),
    path('upload/', views.upload, name="upload")
]
