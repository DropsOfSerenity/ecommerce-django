from django.conf.urls import include, url


urlpatterns = [
    url(r'^$', 'products.views.index', name='index'),
    url(r'^(?P<slug>[-\w]+)/$', 'products.views.show', name='detail'),  
]
