from django.conf.urls import url

from . import views

app_name = 'books'

urlpatterns = [
   # url(r'^$', views.index, name='index'),
   # url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
   url(r'^$', views.IndexView.as_view(), name='index'),
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
url(r'^book/add$', views.CreateView.as_view(), name='book-add'),
]