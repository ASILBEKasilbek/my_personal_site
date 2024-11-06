from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('blog/',blog,name='blog'),
    path('portfolio/',portfolio),
    path('about/',about),
    path('blog/<int:pk>/',blog_detail,name='blog_detail')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

