from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^contact/', views.contact , name='contact'),
    url(r'^story/', views.story , name='story'),
    url(r'^picture/', views.picture , name='picture'),
    url(r'^video/', views.video, name='video'),
    url(r'^blog/', views.blog, name='blog'),
]
