from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage, name="homepage"),
    url(r'^view/(?P<pk>\d+)/$',views.video,name="ViewVideo"),  
    path('accounts/', include('allauth.urls')),
    path('upload/', views.upload, name="upload"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
