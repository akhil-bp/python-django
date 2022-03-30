from urllib.parse import urlparse
from django.urls import URLPattern, path
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('detail', views.detail, name="detail"),
    path('list-all', views.listAll, name="listAll")
]
# name optional