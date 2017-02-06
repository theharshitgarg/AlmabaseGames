from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list$', views.GamesListView.as_view(), name='index'),    
]
