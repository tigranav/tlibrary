from django.conf.urls import url

from . import views

app_name = 'books'

urlpatterns = [
   # url(r'^$', views.index, name='index'),
   # url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),
   url(r'^$', views.IndexView.as_view(), name='index'),
   url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
   url(r'^book/add$', views.CreateView.as_view(), name='book-add'),
   url(r'^book/(?P<pk>[0-9]+)/$', views.UpdateView.as_view(), name='book-update'),
   url(r'^book/(?P<pk>[0-9]+)/delete/$', views.DeleteView.as_view(), name='book-delete'),

]