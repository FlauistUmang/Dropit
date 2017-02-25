from django.conf.urls import url
from . import views
from share import views as share_views

urlpatterns = [
    url(r'^signup/', views.signup, name='signup'),
    url(r'^login/', views.login, name='login'),
    url(r'^upload/', share_views.upload, name='upload'),
    url(r'^logout', views.logout, name='logout'),
]