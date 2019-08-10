
from django.conf.urls import include,url
from django.contrib import admin
from hhomeworkapp import views


urlpatterns = [
    url(r'^admin/',include(admin.site.urls)),
    url(r'^$', views.Contactview),
    url(r'^data/', views.FatchingData)
]
